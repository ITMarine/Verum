import uuid
import pika
import sys
import os
import collections

collections.Callable = collections.abc.Callable


def main():

    def reverse_and_save(source_text):
        output_text = f"input: {source_text} output: {source_text[::-1]}\n"
        storage = "../storage/storage" + f"{str(uuid.uuid4())}"
        unsent = "../unsent/unsent_queue"
        with open(storage, 'a') as f:
            f.write(output_text)
        with open(unsent, 'a') as f:
            f.write(output_text)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='reverse')

    def callback(ch, method, properties, body):
        source_text = body.decode()
        print(" [x] Received %r" % source_text)
        reverse_and_save(source_text)

    channel.basic_consume('reverse', callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
