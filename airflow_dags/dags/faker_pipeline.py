from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("faker_pipeline",
         start_date=datetime(2025, 1, 1),
         schedule_interval="@daily",
         catchup=False) as dag:

    task_create_faker_data = BashOperator(
        task_id="create_faker_data",
        bash_command="python /opt/airflow/dags/faker_data.py"
    )
