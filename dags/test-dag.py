import logging
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': "2020-01-01",
}

with DAG(
    'dag',
    default_args=default_args,
    description='A  DAG',
    schedule_interval=None,
) as dag:

    t1 = PythonOperator(task_id='t1', python_callable=lambda : logging.info("in t1"))
    t2 = PythonOperator(task_id='t2', python_callable=lambda : logging.info("in t2"))
    
    t1 >> t2