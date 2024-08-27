from airflow import DAG
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_xcom_eg2",
    schedule="30 6 * * *", # 매일 아침 6시 30분
    start_date=pendulum.datetime(2024, 8, 24, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    @task(task_id='python_xcom_push_by_return')
    def xcom_push_result(**kwargs):
        return 'Success'
    
    @task(task_id='python_xcom_pull_1')
    def xcom_pull_1(**kwargs):
        ti = kwargs['ti']
        value1 = ti.xcom_pull(task_ids='python_xcom_push_by_return')
        print(f"xcom_pull method로 직접 찾은 return value: {value1}")

    @task(task_id='python_xcom_pull_2')
    def xcom_pull_2(status, **kwargs):
        print(f'함수 입력값으로 받은 값: {status}')

    
    python_xcom_push_by_return = xcom_push_result()
    xcom_pull_2(python_xcom_push_by_return)
    python_xcom_push_by_return >> xcom_pull_1()