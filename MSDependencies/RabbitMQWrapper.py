import pika
import json
from ReportHandler.ChecksDependencies import ChecksDependencies

class RabbitMQWrapper:

    def __init__(self, url):
        self.connection = pika.BlockingConnection(pika.connection.URLParameters(url=url))
        self.channel = None

    def send(self, queue, durable, body, routing_key):
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue, durable=durable)
        self.channel.basic_publish(body=body, exchange='', routing_key=routing_key)

    def listen(self, queue):
        def callback(ch, method, properties, body): #Body: json en str
            resp = json.loads(body.decode('utf8'))
            if resp["git_url"] is None:
                resp["git_url"] = 'https://github.com/BaptisteMagoni/app-questionnaire-vue.git'
            print(resp['git_url'])
            check = ChecksDependencies(resp["git_url"])  # Instanciation pour récupérer les dépendences du projet et fonction de sont chemin ou url
            check.start()  # Permet de lancer la recherche
            resp["report"] = check.getReport()
            print(resp["report"])
            if check.report.hasOutdatedPackage():
                self.send(queue='alert', durable=True, body=json.dumps(check.getReport()), routing_key='alert')  # Envoie le rapport dans la queue alert

        self.channel = self.connection.channel()
        self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()