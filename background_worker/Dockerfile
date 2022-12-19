FROM python:alpine

WORKDIR /app

RUN pip install pika

COPY . .

CMD ["python3", "background_worker.py"]