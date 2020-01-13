from .models import User, FrequenceList, RapportInfo, Rapport
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .rapportInfoChecker.checkerGitHubRapport import CheckerGitHubRapport
import pika

# Dans ce fichier nous déclarons les attributs pour l'API REST en fonction des models existants

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'libelle_git', 'Discord_webHook', 'Slack_webHook']

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        username = request.session['username']
        data = []
        try:
            queryset = User.objects.get(libelle_git=username)
            serializer = UserSerializer(queryset, many=False)
            data = serializer.data
        except:
            pass
        return Response(data)

class FrequenceListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FrequenceList
        fields = ['id', 'libFrequence', 'stateFrequence']

class FrequenceListSet(viewsets.ModelViewSet):
    queryset = FrequenceList.objects.all()
    serializer_class = FrequenceListSerializer

    def list(self, request):
        # RapportInfo.objects.get(user=User.objects.get(libelle_git='ncev'))
        queryset = FrequenceList.objects.all()
        serializer = FrequenceListSerializer(queryset, many=True)
        return Response(serializer.data)

class RapportInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RapportInfo
        fields = ['repo_link', 'repo_name', 'hasAutoReport', 'Discord_alert', 'Slack_alert', 'frequence', ]

class RapportInfoSet(viewsets.ModelViewSet):
    queryset = RapportInfo.objects.all()
    serializer_class = RapportInfoSerializer

    def list(self, request):
        username = request.session['username']
        checker = CheckerGitHubRapport()

        return Response(checker.check(username))

    def retrieve(self, request, pk=None):
        queryset = RapportInfo.objects.get(id=1)
        serializer = RapportInfoSerializer(queryset, many=False)
        return Response(serializer.data)

class RapportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rapport
        fields = ['id', 'dateRapport', 'content']

class RapportSet(viewsets.ModelViewSet):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer

    def list(self, request):
        queryset = Rapport.objects.all()
        serializer = RapportSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        print('test')
        return Response()
