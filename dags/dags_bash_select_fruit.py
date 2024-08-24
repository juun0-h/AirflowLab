from airflow import DAG
import pendulum, datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="10 0 * * 6#1",    # 매월 첫번째 주 토요일 0시 10분
    start_date=pendulum.datetime(2024, 8, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    t1_orange = BashOperator(
        task_id="t1_orange",
        bash_command="/opt/AirflowLab/plugins/shell/selec_fruit.sh ORANGE"
    )
    t2_avocado = BashOperator(
        task_id="t2_avocado",
        bash_command="/opt/AirflowLab/plugins/shell/selec_fruit.sh ORANGE"
    )

    t1_orange >> t2_avocado