FROM python:alpine

WORKDIR /app

RUN pip install fastapi uvicorn pika

EXPOSE 8000

COPY . .

CMD ["uvicorn", "http_api:app", "--host", "0.0.0.0", "--port", "8000"]
