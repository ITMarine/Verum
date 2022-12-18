import asyncio
import pika
from fastapi import FastAPI, Body


app = FastAPI()


@app.post("/queue_reverse_text/")
async def queue_reverse_text(source_text=Body()) -> None:
    if source_text:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='reverse')
        channel.basic_publish(exchange='',
                              routing_key='reverse',
                              body=source_text)
        print("[x] sent source text")
        connection.close()
    return source_text
