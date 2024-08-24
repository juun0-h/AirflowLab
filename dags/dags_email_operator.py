from airflow import DAG
import datetime
import pendulum
from airflow.operators.email import EmailOperator


with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2024, 8, 1, tz="Asia/Seoul"), # tz="UTC": 국제표준시간
    catchup=False,
) as dag:
    send_email_task = EmailOperator(
        task_id="send_email_task",
        to="expershyp33@naver.com",
        subject="Airflow email test",
        html_content="Airflow task completed!"
    )