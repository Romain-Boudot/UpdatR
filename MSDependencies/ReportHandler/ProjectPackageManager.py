#!/usr/bin/python37
# -*- coding: utf-8 -*-

import os

class PackageManager:

    def __init__(self, path):
        self.path = path
        self.type = "npm"

    def getTypeProjectManage(self):
        return self.type

    def searchTypeProjectManager(self):
        for file in os.listdir(self.path):
            print(file)