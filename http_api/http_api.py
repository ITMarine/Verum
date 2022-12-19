import pika
from fastapi import FastAPI, Body


app = FastAPI()


@app.get("/queue_reverse_text")
async def queue_reverse_text(source_text: str) -> str:
    """receives source text from queue_reverse_text.py
    then sends it into rabbitMQ queue"""
    if source_text:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
        channel = connection.channel()
        channel.queue_declare(queue='reverse', durable=True)
        channel.basic_publish(exchange='',
                              routing_key='reverse',
                              body=source_text)
        connection.close()
    return source_text
