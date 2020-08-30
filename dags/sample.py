import random

from airflow import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(2),
}

with DAG(
    'sample',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=None,
) as dag:

    tasks = []

    for i in range(20):
        tasks.append(BashOperator(task_id=f"task_{i}", bash_command=f"sleep {random.randint(0,60)}"))


    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )


t1 >> tasks
