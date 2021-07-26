# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /opt

ADD . /opt

RUN pip install -r requirements.txt

CMD [ "python", "-u", "./opt/app.py"]