FROM python:3.7

LABEL authors="Ricky Danipog , Ronen Rozen"

COPY . /app

WORKDIR /app

ARG MODE

ENV MODE=${MODE}

RUN pip install --no-cache-dir  -r requirements.txt

EXPOSE 5000

CMD ["sh", "-c", "python run.py $MODE"]