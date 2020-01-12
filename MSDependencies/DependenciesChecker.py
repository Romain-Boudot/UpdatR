#!/usr/bin/python37
# -*- coding: utf-8 -*-

from RabbitMQWrapper import RabbitMQWrapper
from ReportHandler.ChecksDependencies import ChecksDependencies

if __name__ == "__main__":
    """url = "amqp://guest:Romain01@app.updatr.tech"
    rabbit = RabbitMQWrapper(url=url) #Instanciation pour lire les queues
    rabbit.listen('url_git') #Lit les queues"""
    check = ChecksDependencies(path="https://github.com/BaptisteMagoni/app-questionnaire-vue.git")
    check.start()