FROM python:3.7-alpine
MAINTAINER Aaron  

ENV PYTHONUNBUFFERD 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
