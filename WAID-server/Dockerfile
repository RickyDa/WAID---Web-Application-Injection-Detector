FROM python:3.7
LABEL authors="Ricky Danipog , Ronen Rozen"

COPY . /app

WORKDIR /app

ARG MODE

RUN pip install --no-cache-dir  -r requirements.txt

EXPOSE 5000

RUN python run.py $MODE
