from time import sleep
from concurrent.futures import ThreadPoolExecutor
from airflow.plugins_manager import AirflowPlugin
from airflow.executors.base_executor import BaseExecutor

import docker

import logging

def get_state(container):

    container.reload()
    status = container.attrs['State']['Status']
    exitcode = container.attrs['State']['ExitCode']

    return status, exitcode

def submit_docker_batch_job(cmd):

    client = docker.DockerClient(base_url='unix://opt/airflow/docker.sock')
    volumes = {
        "/Users/hj/airflow_batch_executor/dags": {"bind":"/opt/airflow/dags",'mode': 'ro'},
        "/Users/hj/airflow_batch_executor/logs":{"bind":"/opt/airflow/logs",'mode': 'rw'},
    }
    environment = {
        "AIRFLOW__CORE__SQL_ALCHEMY_CONN":"postgresql://airflow:airflow@metadata-db:5432/airflow"
    }

    container = client.containers.run(
        "airflow_batch_executor_airflow-scheduler:latest", 
        cmd, 
        detach=True, 
        network="airflow_batch_executor_default", 
        volumes=volumes, 
        environment=environment
    )

    while get_state(container)[0] == 'running':
        sleep(0.1)

    if get_state(container) == ('exited',0):
        container.reload()
        return container.logs()
    else:
        container.reload()
        raise RuntimeError(container.logs())

class HjExecutor(BaseExecutor):

    def __init__(self):
        super().__init__()
        logging.info("INIT EXECUTOR")

        self.pool = ThreadPoolExecutor(10)
        self.futures = {}

    def execute_async(self, key, command, queue=None, executor_config=None):
        logging.info("EXECUTE ASYNC")
        logging.info(f"{self=}\n,{key=},\n{command=}")

        future = self.pool.submit(submit_docker_batch_job, command[1:])
        self.futures[future] = key


    def process_future(self, future):
        
        if future.done():
            key = self.futures[future]
            if future.exception():
                logging.info(future.exception())
                self.fail(key)
            elif future.cancelled():
                self.fail(key)
            else:
                self.success(key)
            self.futures.pop(future)


    def sync(self):
        logging.info("SYNC")
        for future in self.futures.copy():
            self.process_future(future)


class HjPlugin(AirflowPlugin):
  name = 'hj'
  executors = [HjExecutor]