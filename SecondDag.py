#!/usr/bin/python3
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# let's setup arguments for our dag

my_dag_id = "my_second_dag"

default_args = {
    'owner': 'rajeev',
    'depends_on_past': False,
    'retries': 10,
    'concurrency': 1
}

# dag declaration

dag = DAG(
    dag_id=my_dag_id,
    default_args=default_args,
    start_date=datetime(2022, 9, 10),
    schedule_interval=timedelta(seconds=5)
)


# Here's a task based on Bash Operator!

bash_task = BashOperator(task_id='bash_task_1',
                         bash_command="echo 'Hello Airflow from the git repo ..!!!'",
                         dag=dag)
