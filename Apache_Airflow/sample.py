from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


# Define Python functions for tasks
def start_task():
    print("Starting the workflow!")


def process_data():
    print("Processing data...")


def end_task():
    print("Workflow completed!")


# Define the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}

with DAG(
    dag_id="simple_example_dag",  # Unique identifier for the DAG
    default_args=default_args,
    description="A simple DAG example",
    schedule_interval=None,  # Manually triggered
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # Define tasks
    start = PythonOperator(
        task_id="start_task",  # Unique identifier for the task
        python_callable=start_task,
    )

    process = PythonOperator(
        task_id="process_task",
        python_callable=process_data,
    )

    end = PythonOperator(
        task_id="end_task",
        python_callable=end_task,
    )

    # Task dependencies
    start >> process >> end
