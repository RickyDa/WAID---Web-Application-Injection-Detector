FROM python:3.7
LABEL authors="Ricky Danipog , Ronen Rozen"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]