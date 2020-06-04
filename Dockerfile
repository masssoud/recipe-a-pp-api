FROM python:3.7-alpine
MAINTAINER Masoud Najafi


ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.tx

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user