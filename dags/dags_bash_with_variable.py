from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.models import Variable

with DAG(
    dag_id='dags_bash_with_variable',
    schedule='10 9 * * *',
    start_date=pendulum.datetime(2024, 8, 24, tz='Asia/Seoul'),
    catchup=False
) as dag:
    var_value = Variable.get("sample_key")

    bash_var1 = BashOperator(
        task_id='bash_var1',
        bash_command=f'echo Variable: {var_value}'
    )

    bash_var2 = BashOperator(
        task_id='bash_var2',
        bash_command='echo Variable: {{ var.value.sample_key }}'
    )

    