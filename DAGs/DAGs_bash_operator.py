from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="DAGs_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 3, 1, tz="Asia/Seoul"), # tz="UTC": 국제표준시간
    catchup=False,
    # dagrun_timeout=datetime.timedelta(minutes=60),  # run time out 설정
    # tags=["example", "example2"],
    # params={"example_key": "example_value"},
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    bash_t2 = BashOperator(
        task_id="bash_t1",
        bash_command="echo $HOSTNAME",
    )
    
    bash_t1 >> bash_t2  # 실행 순서