import pika
import json
from ..models import Rapport

class ReadRapport:
    def __init__(self, url):
        self.connection = pika.BlockingConnection(pika.connection.URLParameters(url=url))
        self.channel = None

    def send(self, queue, durable, body, routing_key):
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue, durable=durable)
        self.channel.basic_publish(body=body, exchange='', routing_key=routing_key)

    def listen(self, queue):
        def callback(ch, method, properties, body):
            rapport = Rapport()
            rapport.content = body
            rapport.save()

        self.channel = self.connection.channel()
        self.channel.basic_consume(
            queue=queue, on_message_callback=callback, auto_ack=True)
