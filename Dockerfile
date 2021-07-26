FROM python:3.8

COPY . /opt

WORKDIR /opt
ADD / /opt

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]
