
import os
import shutil

class GitUser:

    def __init__(self, url):
        self.url = url
        self.name = self.getNameProject()
        self.path = None

    def getNameProject(self):
        tab = str(self.url).split("/")
        return str(tab[len(tab)-1]).replace(".git", "")

    def clone(self):
        os.chdir("./repos")
        os.system("git clone {}".format(self.url))
        self.path = "../repos/{}".format(self.name)
        return self.path

    def remove(self, path):
        shutil.rmtree(path, ignore_errors=True)