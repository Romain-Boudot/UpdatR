#!/usr/bin/python37
# -*- coding: utf-8 -*-

from RabbitMQWrapper import RabbitMQWrapper
from ReportHandler.ChecksDependencies import ChecksDependencies
import os

if __name__ == "__main__":
    os.chdir("./repos")
    while True:
        url = "amqp://guest:Romain01@app.updatr.tech"
        rabbit = RabbitMQWrapper(url=url) #Instanciation pour lire les queues
        rabbit.listen('url_git') #Lit les queues

    """check = ChecksDependencies(path="https://github.com/BaptisteMagoni/app-questionnaire-vue.git")
    check.start()"""