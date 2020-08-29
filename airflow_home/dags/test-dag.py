from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

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

    t1 = DummyOperator(
        task_id='t1',
    )

    t1.doc_md = """
    # This is a DAG - go to [google](http://www.google.com)
    """


    t2 = DummyOperator(
        task_id='t2',
    )

    t2.doc_md = """
    # This is a DAG - go to [google](http://www.google.com)
    """
    
    t1 >> t2