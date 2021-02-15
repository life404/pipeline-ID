#! /usr/bin/env python3

import uuid

class Search():
    def __init__(self):
        self.path = ""
        self.commit = ""
        self.name = ""
        self.parent = ""
        self.uuid = ""
        self.update = ""
        
    def ADD(self, path, commit, name, parent, uuid):
        self.path = path
        self.commit = commit
        self.name = name
        self.parent = parent
        self.uuid = uuid

    def UPDATE(self, uuid, update):
        self.uuid = uuid
        self.update = update

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

    def Info(self):
        print("Search Name: " + self.Name())
        print("Search Path: " + self.Path())
        print("Search UUID: " + self.Uuid())
        print("Search Commit: " + self.Commit())
        print("Search Parent: " + self.Parent())
    
    def Update(self):
        return self.update
    



