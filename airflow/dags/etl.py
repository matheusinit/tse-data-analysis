from datetime import datetime
from airflow import DAG

from airflow.providers.papermill.operators.papermill import PapermillOperator

with DAG(
    dag_id='elections_2022',
    default_args={
        'retries': 0
    },
    schedule='0 0 * * *',
    start_date=datetime(2022, 10, 1),
    template_searchpath='/usr/local/airflow/include',
    concurrency=1,
    catchup=False
) as dag_1:
    ingestion = PapermillOperator(
        task_id="ingestion",
        input_nb="../../pipelines/00_ingestion.ipynb",
        output_nb="out/00_ingestion_out_{{ execution_date }}.ipynb",
        parameters={"execution_date": "{{ execution_date }}"},
    )

    cleansing = PapermillOperator(
        task_id="ingestion",
        input_nb="../../pipelines/01_cleansing.ipynb",
        output_nb="out/01_cleansing_out_{{ execution_date }}.ipynb",
        parameters={"execution_date": "{{ execution_date }}"},
    )

    ingestion >> cleansing