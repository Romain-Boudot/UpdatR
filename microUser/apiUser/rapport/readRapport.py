import pika
import json
from ..models import Rapport

RABBIT = {
    'URL': 'amqp://guest:Romain01@app.updatr.tech',
    'QUEUE_LISTEN': 'rapport',
    'QUEUE_EMIT': 'url_git'
}

class ReadRapport:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.connection.URLParameters(url=RABBIT['URL']))
        channel = self.connection.channel()

        channel.queue_declare(queue=RABBIT['QUEUE_EMIT']) # nous déclarons la queue d'écoute

        channel.basic_consume(queue=RABBIT['QUEUE_LISTEN'], # nous déclarons la queue d'emission
                      auto_ack=True,
                      on_message_callback=self.callback)
        self.channel = channel

    def send(self, body, routing_key=''):
        self.channel.basic_publish(body=body, exchange='', routing_key=routing_key)

    def callback(self, ch, method, properties, body):
        rapport = Rapport()
        rapport.content = body
        rapport.save()

instance = None
def setReadRapport(inst):
    global instance
    instance = inst

def getReadRapport():
    global instance
    return instance