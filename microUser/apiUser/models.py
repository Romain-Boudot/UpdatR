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
    repo_name = models.CharField(max_length=255, null=True)
    frequence = models.IntegerField()
    Discord_alert = models.CharField(max_length=255, default='')
    Slack_alert = models.CharField(max_length=255, default='')
    # DateTimeRapport = models.DateTimeField()
    hasAutoReport = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Rapport(models.Model):
    dateRapport = models.DateField(null=True, auto_now_add=True)
    content = models.TextField()
    repo_link = models.CharField(max_length=255)
    rapportInfo = models.ForeignKey(RapportInfo, on_delete=models.CASCADE, null=True)
