FROM apache/airflow:2.9.2

RUN pip install apache-airflow-providers-papermill

USER airflow
