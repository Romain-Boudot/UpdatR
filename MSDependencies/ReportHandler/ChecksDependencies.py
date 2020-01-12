#!/usr/bin/python37
# -*- coding: utf-8 -*-

import os
import subprocess
from ReportHandler.ProjectPackageManager import PackageManager
from ReportHandler.Report import Report
from Git.GitUser import GitUser
import subprocess

COMMAND = {
    "windows": {
        "npm": "cd {}; npm outdated --long --json"
    },
    "Linux": {
        "npm": "cd {} && npm outdated --long --json"
    }
}


class ChecksDependencies:

    def __init__(self, path=None):
        self.path = path
        self.pm = PackageManager(self.path)
        self.projectType = self.pm.getTypeProjectManage()
        self.infoProject = {}
        self.report = Report()
        self.git = GitUser(path)
        self.path_git = self.git.clone()

    def start(self):
        self.loadReports()
        print(self.getReport())
        # self.git.remove(self.path_git)

    def loadReports(self):
        self.report.loadReports(self.getDependeciesJson())

    def getReport(self):
        return self.report.getReport()

    def getOsName(self):
        try:
            return os.uname().sysname
        except:
            return "windows"

    def getDependeciesJson(self):
        osName = self.getOsName()
        command = COMMAND[osName][self.projectType].format(self.path_git)
        if osName == "windows":
            return subprocess.getoutput('powershell.exe {}'.format(command))
        elif osName == "Linux":
            return self.bashCommand(command)
        return None
        # return subprocess.getoutput('powershell.exe {}'.format(command))

    def getInfoProject(self):
        return self.infoProject

    def getName(self):
        try:
            return self.infoProject['name']
        except ValueError:
            return False

    def getVersion(self):
        try:
            return self.infoProject['version']
        except ValueError:
            return False

    def getVisibility(self):
        try:
            return self.infoProject['visibility']
        except ValueError:
            return False

    def getDependencies(self):
        try:
            return self.infoProject['dependencies']
        except ValueError:
            return False

    def bashCommand(self, str_):
        process = subprocess.Popen(str_, stdout=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        return output.decode('UTF-8')