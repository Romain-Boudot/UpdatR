#!/usr/bin/python37
# -*- coding: utf-8 -*-

import request
import json
class Report:

    #npm list <package>

    """report = {
        "discord.js":  {
            "packageVersion": "",
            "lastVersion": "",
            "url": "...",
            "doc": "..",
            "packageType": "...",
            "homepage": "...",
            "outdated": bool
        }
    }"""

    def __init__(self):
        self.reports = {}

    def loadReports(self, listDependencies):
        rep = json.loads(listDependencies)
        for package in rep:
            name = str
            if str(package).startswith("@vue"):
                name = str(package).split('/')[1]
            else:
                name = package

            packageVersion = rep[package]['current']
            lastVersion = rep[package]['latest']
            packageType = rep[package]['type']
            homePage = rep[package]['homepage']
            url = "https://www.npmjs.com/package/{}".format(name)
            outdated = self.isOutdated(packageVersion, lastVersion)
            self.reports[name] = {
                "packageVersion": packageVersion,
                "lastVersion": lastVersion,
                "url": url,
                "outdated": outdated,
                "packageType": packageType,
                "homePage": homePage
            }

    def isOutdated(self, actualVersion, lastVersion):
        tabActualVersion = str(actualVersion).split('.')
        tabLastVersion = str(lastVersion).split('.')

        for i in range(3):
            if int(tabActualVersion[i]) < int(tabLastVersion[i]):
                return False
        return True

    def getReport(self):
        return self.reports