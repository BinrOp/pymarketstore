FROM continuumio/miniconda3

COPY requirements.txt /
RUN pip install -r /requirements.txt

ADD tests /tests

WORKDIR /tests
