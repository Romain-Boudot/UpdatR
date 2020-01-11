
import os
import shutil

class GitUser:

    def __init__(self, url):
        self.url = url

    def clone(self):
        os.chdir("./repos")
        os.system("git clone {}".format(self.url))
        return "../repos/{}".format("app-questionnaire-vue")

    def remove(self, path):
        shutil.rmtree(path, ignore_errors=True)