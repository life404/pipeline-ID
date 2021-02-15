#! /usr/bin/env python3

import sqlite3
import os
from Search import *

class SQL():
    def __init__(self, Search, dbname):
        self.Search = Search
        self.dbname = dbname
        self.sql_path = os.path.join(os.getcwd(), self.dbname)

    def Init(self):
        self.connection = sqlite3.connect(self.sql_path)
        self.cursor = self.connection.cursor()
        create_tbl = "CREATE TABLE IF NOT EXISTS PPID_CONTENT (Uuid TEXT PRIMARY KEY, Path TEXT, Name TEXT, Content TEXT, Parent TEXT)"
        self.cursor.execute(create_tbl)
    
    def Close(self):
        self.connection.commit()
        self.connection.close()

    def Remove(self):
        switch = input("Do you really want to remove %s [Y]es/[N]o:" %(self.dbname))
        if switch == "Y":
            os.remove(os.path.join(os.getcwd(), self.dbname))
            print("The %s had beed removed." % (self.dbname))
        elif switch == "N":
            exit(0)
        else:
            print("Please input 'Y' or 'N'")
            exit(1)
        
    def Add(self):
        self.Init()
        add_value = ("INSERT INTO PPID_CONTENT VALUES ('%s', '%s', '%s', '%s', '%s')" %(self.Search.Uuid(),
                                                                                        self.Search.Path(),
                                                                                        self.Search.Name(),
                                                                                        self.Search.Commit(),
                                                                                        self.Search.Parent()))
        self.cursor.execute(add_value)
        self.Close()

    def Update(self):
        self.Init()
        update_list = self.Search.Update().split(";")
        for update_pair in update_list:
            update_name = update_pair.split(":")[0]
            update_value = update_pair.split(":")[1]
            update = ("UPDATE PPID_CONTENT SET %s='%s' WHERE Uuid='%s'" %(update_name, update_value, self.Search.Uuid()))
            print(update)
            self.cursor.execute(update)

        self.Close()