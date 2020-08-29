from airflow.plugins_manager import AirflowPlugin
from airflow.executors.base_executor import BaseExecutor
from airflow.operators import BaseOperator

import logging

class HjExecutor(BaseExecutor):

    def __init__(self):
        super().__init__()
        logging.info("INIT EXECUTOR")

    def execute_async(self, key, command, queue=None, executor_config=None):
        logging.info("EXECUTE ASYNC")
        logging.info(f"{self=}\n,{key=},\n{command=}")

    def sync(self):
        logging.info("SYNC")


class HjPlugin(AirflowPlugin):
  name = 'hj'
  executors = [HjExecutor]