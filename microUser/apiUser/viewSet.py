from .models import User, FrequenceList, RapportInfo, Rapport
from rest_framework import serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'libelle_git', 'Discord_webHook', 'Slack_webHook']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FrequenceListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FrequenceList
        fields = ['id', 'libFrequence', 'stateFrequence']

class FrequenceListSet(viewsets.ModelViewSet):
    queryset = FrequenceList.objects.all()
    serializer_class = FrequenceListSerializer

class RapportInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RapportInfo
        fields = ['id', 'repo_link', 'frequence', 'Discord_alert', 'Slack_alert', 'DateTimeRapport', 'user']

class RapportInfoSet(viewsets.ModelViewSet):
    queryset = RapportInfo.objects.all()
    serializer_class = RapportInfoSerializer

class RapportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rapport
        fields = ['id', 'content']

class RapportSet(viewsets.ModelViewSet):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer

