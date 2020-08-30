FROM apache/airflow:1.10.12-python3.8

USER root

# install extra deps
RUN pip install docker awswrangler bulwark gspread_pandas

## install plugin
COPY hj_plugin /hj_plugin
RUN pip install /hj_plugin

RUN chown airflow /opt/airflow/

USER airflow