import pika
import json
from ..models import Rapport, RapportInfo

RABBIT = {
    'URL': 'amqp://guest:Romain01@app.updatr.tech',
    'QUEUE_LISTEN': 'rapport',
    'QUEUE_EMIT': 'url_git'
}

class ReadRapport:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.initChannel()
        
    def initChannel(self):
        self.connection = pika.BlockingConnection(pika.connection.URLParameters(url=RABBIT['URL']))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=RABBIT['QUEUE_EMIT']) # nous déclarons la queue d'emission

        channel = self.connection.channel()
        channel.basic_consume(queue=RABBIT['QUEUE_LISTEN'], # nous déclarons la queue d'ecoute
                      auto_ack=True,
                      on_message_callback=self.callback)
        channel.start_consuming()
        # self.channel = channel

    def send(self, body):
        route = RABBIT['QUEUE_EMIT']
        js = json.dumps(body)
        self.sendData(js, route)

    def sendData(self, js, route):
        self.channel.basic_publish(exchange='', routing_key=route, body=js)
        # self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        try:
            content = body.decode('utf8')
            js = json.loads(content)
            repo_link = js['git_url']
            data = js['rapportInfo']
            rapport = Rapport()
            rapport.content = data
            rapport.rapportInfo = self.getRapportInfoById(repo_link)
            rapport.save()
        except:
            pass
        finally:
            self.channel.stop_consuming()
            self.initChannel()
    
    def getRapportInfoById(self, repo_link):
        try:
            return RapportInfo.objects.get(repo_link=repo_link)
        except:
            return None

instance = None
def setReadRapport(inst):
    global instance
    instance = inst

def getReadRapport():
    global instance
    return instance
