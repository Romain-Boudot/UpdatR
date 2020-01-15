from ..tools.getURL import getJSON
from ..models import RapportInfo, User
import collections

class CheckerGitHubRapport:
    def __init__(self):
        pass

    def check(self, username):
        from ..viewSet import RapportInfoSerializer
        rapportInfos = self.getRapportInfosByUserLibelleGit(username)
        
        # https://api.github.com/users/ncev/repos
        githubRepos = getJSON('https://api.github.com/users/' + username + '/repos')
        supDatas = self.orderRapports(rapportInfos, githubRepos)
        orderedSupDatas = self.convertDictToOrderectDict(supDatas)
        rapportInfosData = RapportInfoSerializer(rapportInfos, many=True).data
        orderedSupDatas.extend(rapportInfosData)
        return orderedSupDatas

    def convertDictToOrderectDict(self, dict):
        orderedDicts = []
        for d in dict:
            orderedDicts.append(collections.OrderedDict(d))
        return orderedDicts

    def orderRapports(self, rapportInfos, githubRepos):
        datas = []
        for repos in githubRepos:
            if not self.isRapportWIthRepoName(rapportInfos, repos['name']):
                datas.append({'repo_link': repos['url'], 'repo_name': repos['name'], 'hasAutoReport': False})

        return datas
    
    def isRapportWIthRepoName(self, rapportInfos, name):
        for rapportInfo in rapportInfos:
            if rapportInfo.repo_name == name:
                return True
        return False

    def getUserByLibelleGit(self, libelle_git):
        try:
            return User.objects.get(libelle_git=libelle_git)
        except:
            return None

    def getRapportInfosByUserLibelleGit(self, libelle_git):
        user = self.getUserByLibelleGit(libelle_git)
        if user == None:
            user = User()
            user.libelle_git = libelle_git
            user.save()
            user = self.getUserByLibelleGit(libelle_git)
        try:
            return RapportInfo.objects.filter(user=user)
        except:
            return []
