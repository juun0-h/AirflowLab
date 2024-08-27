from airflow import DAG
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_xcom_eg1",
    schedule="30 6 * * *", # 매일 아침 6시 30분
    start_date=pendulum.datetime(2024, 8, 24, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    @task(task_id='python_xcom_push_task1')
    def xcom_push1(**kwargs):
        ti = kwargs['ti']
        # XCom push
        ti.xcom_push(key='res1', value='val1')
        ti.xcom_push(key='res2', value=[1, 2, 3])
    
    @task(task_id='python_xcom_push_task2')
    def xcom_push2(**kwargs):
        ti = kwargs['ti']
        # XCom push
        ti.xcom_push(key='res1', value='val3')
        ti.xcom_push(key='res2', value=[1, 2, 3, 4])
    
    @task(task_id='python_xcom_pull_task')
    def xcom_pull(**kwargs):
        ti = kwargs['ti']
        # XCom pull
        value1 = ti.xcom_pull(key='res1')
        value2 = ti.xcom_pull(key='res2', task_ids=['python_xcom_push_task1'])
        print(f"value1: {value1}")
        print(f"value2: {value2}")
    
    xcom_push1() >> xcom_push2() >> xcom_pull()