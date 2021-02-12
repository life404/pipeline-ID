#! /usr/bin/env python3

import sys
import os
import uuid

class Search():
    def __init__(self, path, commit, name, parent, uuid):
        self.path = path
        self.commit = commit
        self.name = name
        self.parent = parent
        self.uuid = uuid

    def Uuid(self):
        if self.uuid:
            return self.uuid
        else:
            return str(uuid.uuid3(uuid.NAMESPACE_DNS, self.path))
    
    def Commit(self):
        if self.commit:
            return self.commit
        else:
            return "..."

    def Parent(self):
        if self.parent:
            return self.parent
        else:
            return "..."
    
    def Name(self):
        if self.name:
            return self.name
        else:
            return self.Uuid()
    
    def Path(self):
        return self.path

    def info(self):
        print("Search Name: " + self.Name())
        print("Search Path: " + self.Path())
        print("Search UUID: " + self.Uuid())
        print("Search Commit: " + self.Commit())
        print("Search Parent: " + self.Parent())


