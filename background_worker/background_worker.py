import pika
import sys
import os
import time
import collections

collections.Callable = collections.abc.Callable

STORAGE = "/app/storage/storage"
UNSENT = "/app/unsent/unsent_queue"


def main():

    def reverse_and_save(source_text):
        output_text = f"input: {source_text} output: {source_text[::-1]}\n"
        with open(STORAGE, 'a') as f:
            f.write(output_text)
        with open(UNSENT, 'a') as f:
            f.write(output_text)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', port=5672))
    channel = connection.channel()

    channel.queue_declare(queue='reverse', durable=True)

    def callback(ch, method, properties, body):
        source_text = body.decode()
        print(" [x] Received %r" % source_text)
        reverse_and_save(source_text)

    channel.basic_consume('reverse', callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    # time.sleep(9)
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
