from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner':'Aitezaz Akhtar',
    'start_date':days_ago(0),
    'email':'test@test.com',
    'email_on_failure':False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)

}

dag = DAG(
    'my_dag',
    default_args = default_args,
    description = 'My Dag',
    schedule_interval = timedelta(days=1)
)

extract_transform_load = BashOperator(
    task_id = 'extract_transform_load',
    bash_command = '/home/project/airflow/dags/ETL_Server_Access_Log_Processing.sh',
    dag=dag,

)
extract_transform_load


