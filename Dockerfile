FROM apache/airflow:1.10.12-python3.8

USER root

## install plugin
COPY hj_plugin /hj_plugin
RUN pip install /hj_plugin

# install extra deps
RUN pip install docker

RUN chown airflow /opt/airflow/

USER airflow