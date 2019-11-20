#!/usr/bin/python37
# -*- coding: utf-8 -*-

import pika
import json
from ReportHandler.ChecksDependencies import ChecksDependencies

if __name__ == "__main__":
    check = ChecksDependencies("C:/Users/ZasTa/OneDrive/Documents/Cours/Exercice-JS/app-questionnaire-vue/")
    check.start()
    url = "amqp://guest:Romain01@app.updatr.tech"
    connection = pika.BlockingConnection(pika.connection.URLParameters(url=url))
    channel = connection.channel()

    channel.queue_declare(queue='alert', durable=True)
    channel.basic_publish(body=json.dumps(check.getReport()), exchange='', routing_key='alert')