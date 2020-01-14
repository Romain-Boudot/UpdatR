import pika
import json
import os
from ReportHandler.ChecksDependencies import ChecksDependencies

class RabbitMQWrapper:

    def __init__(self, url):
        self.connection = pika.BlockingConnection(pika.connection.URLParameters(url=url))
        self.channel = None
        self.id = {}

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
            print(resp['id'])
            self.id = resp['id']
            try:
                check = ChecksDependencies(resp["git_url"])
                check.start()
                self.reports = {
                    "git_url": resp['git_url'],
                    "rapportInfo": check.getReport()
                }
                print(self.reports)
                if check.report.hasOutdatedPackage():
                    self.send(queue='rapport', durable=False, body=json.dumps(self.reports), routing_key='rapport')  # Envoie le rapport dans la queue alert
                    #os.system("rm -rf {}".format(check.report.path))
            except ValueError:
                pass


        self.channel = self.connection.channel()
        self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
        self.channel.start_consuming()