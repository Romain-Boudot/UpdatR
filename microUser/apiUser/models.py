from django.db import models

class User(models.Model):
    libelle_git = models.CharField(max_length=255, null=True)
    Discord_webHook = models.CharField(max_length=255, null=True)
    Slack_webHook = models.CharField(max_length=255, null=True)

class FrequenceList(models.Model):
    libFrequence = models.CharField(max_length=50)
    stateFrequence = models.DateTimeField()

class RapportInfo(models.Model):
    repo_link = models.CharField(max_length=255)
    frequence = models.IntegerField()
    Discord_alert = models.BooleanField(default=False)
    Slack_alert = models.BooleanField(default=False)
    DateTimeRapport = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Rapport(models.Model):
    content = models.TextField()
