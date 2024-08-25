from airflow import DAG
import datetime
import pendulum
from airflow.operators.python import PythonOperator
from airflow.decorators import task


with DAG(
    dag_id="dags_python_templates",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2024, 8, 20, tz="Asia/Seoul"), # tz="UTC": 국제표준시간
    catchup=False,
) as dag:
    
    # op_kwargs에 Jinja template 변수를 사용하는 PythonOperator
    def func1(start_date, end_date, **kwargs):
        print(f"start_date: {start_date}")
        print(f"end_date: {end_date}")
    
    py_t1 = PythonOperator(
        task_id="py_t1",
        python_callable=func1,
        op_kwargs={'start_date': '{{ data_interval_start | ds }}', 'end_date': '{{ data_interval_end | ds }}'},
    )

    # op_kwargs에서 직접 꺼내서 쓰는 방법
    @task(task_id='py_t2')
    def py_t2(**kwargs):
        print(kwargs)
        print('ds: ', kwargs['ds'])
        print('ts: ', kwargs['ts'])
        print('data_interval_start: ', kwargs['data_interval_start'])
        print('data_interval_end: ', kwargs['data_interval_end'])
        print('task_instances: ', str(kwargs['ti']))

    py_t1 >> py_t2()