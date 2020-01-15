from .models import User, FrequenceList, RapportInfo, Rapport
from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from .rapportInfoChecker.checkerGitHubRapport import CheckerGitHubRapport
from .rapport.readRapport import getReadRapport

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
        fields = ['id', 'repo_link', 'repo_name', 'hasAutoReport', 'Discord_alert', 'Slack_alert', ]

class RapportInfoSet(viewsets.ModelViewSet):
    queryset = RapportInfo.objects.all()
    serializer_class = RapportInfoSerializer

    def list(self, request):
        username = request.session['username']
        checker = CheckerGitHubRapport()
        return Response(checker.check(username))

    def create(self, request):
        username = request.session['username']
        user = User.objects.get(libelle_git=username)
        if not user: 
            return HttpResponse('{ "done": false }')

        rapportInfo = RapportInfo()
        rapportInfo.Discord_alert = request.data['Discord_alert']
        rapportInfo.Slack_alert = request.data['Slack_alert']
        rapportInfo.repo_link = request.data['repo_link']
        rapportInfo.repo_name = request.data['repo_name']
        rapportInfo.hasAutoReport = True
        rapportInfo.user = user
        rapportInfo.save()

        return HttpResponse('{ "done": true }')

    def retrieve(self, request, pk=None):
        queryset = RapportInfo.objects.get(id=1)
        serializer = RapportInfoSerializer(queryset, many=False)
        return Response(serializer.data)

class RapportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rapport
        fields = ['id', 'dateRapport', 'content', 'rapportInfo']

class RapportSet(viewsets.ModelViewSet):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer

    def list(self, request):
        repo_link = request.query_params['repo_link']
        username = request.session['username']

        user = User.objects.get(libelle_git=username)
        if user == None:
            return HttpResponse('[]', content_type="application/json")

        rapportInfos = RapportInfo.objects.filter(user=user)
        rapportInfo = next((rapport for rapport in rapportInfos if rapport.repo_link == repo_link), False)
        if not rapportInfo:
            return HttpResponse('[]', content_type="application/json")

        queryset = Rapport.objects.get(rapport_info=rapportInfo)
        serializer = RapportSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def sendRapport(self, request):
        # id = request.data['rapportInfo']
        print(request.data)
        repo_link = request.data['repo_link']
        # print('pk : ' + pk)
        username = request.session['username']
        checker = CheckerGitHubRapport()
        rapportInfos = checker.check(username)
        rapportInfo = next((rapport for rapport in rapportInfos if rapport['repo_link'] == repo_link), False)

        if not rapportInfo:
            return HttpResponse('{"state": "failed"}', content_type="application/json")

        if not 'Discord_alert' in rapportInfo:
            RapportModel = RapportInfo()
            RapportModel.hasAutoReport = True
            RapportModel.repo_link = rapportInfo['repo_link']
            RapportModel.repo_name = rapportInfo['repo_name']
            if 'Discord_alert' in  request.data:
                RapportModel.Discord_alert = request.data['Discord_alert']
            if 'Slack_alert' in  request.data:
                RapportModel.Slack_alert = request.data['Slack_alert']
            RapportModel.user = User.objects.get(libelle_git=username)
            RapportModel.save()
            rapportInfo = RapportModel

        state = '{"state": "success"}'
        try:
            # rapportInfo = RapportInfo.objects.get(id=id)
            readRapport = getReadRapport()
            content = {
                # 'id': rapportInfo.id,
                'git_url': repo_link, #rapportInfo.repo_link
                'Discord_alert': rapportInfo['Discord_alert'],
                'Slack_alert': rapportInfo['Slack_alert']
            }
            
            readRapport.send(content)
        except ValueError:
            state = '{"state": "failed"}'
        return HttpResponse(state, content_type="application/json")

    def create(self, request):
        if not 'admin' in request.session:
            return self.sendRapport(request)
        admin = request.session['admin']
        if not admin:
            return self.sendRapport(request)

        repo_link = request.data['git_url']
        data = request.data['rapportInfo']
        rapport = Rapport()
        rapport.content = data
        rapport.rapportInfo = RapportInfo.objects.get(repo_link=repo_link)
        rapport.save()
