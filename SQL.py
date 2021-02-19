#! /usr/bin/env python3

import sqlite3
import os
from Search import *
import collections
from icecream import ic

class SQL():
    def __init__(self, Search, dbname):
        self.Search = Search
        self.dbname = dbname
        self.sql_path = os.path.join(os.getcwd(), self.dbname)
        self.level = 1

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
        self.Search.Info()

    def Update(self):
        self.Init()
        update_list = self.Search.Update().split(";")
        for update_pair in update_list:
            update_name = update_pair.split(":")[0]
            update_value = update_pair.split(":")[1]
            update = ("UPDATE PPID_CONTENT SET %s='%s' WHERE Uuid='%s'" %(update_name, update_value, self.Search.Uuid()))
            self.cursor.execute(update)
        self.Close()

    def Select(self):
        self.Init()
        
        if self.Search.uuid == False and self.Search.name != False:
            select = ("SELECT * FROM PPID_CONTENT WHERE Name='%s'" %(self.Search.name))
            self.cursor.execute(select)
            print("%s\t%s\t%s\t%s\t%s" %('Uuid', 'Path', 'Name', 'Commmit', 'Parent'))
            for item in self.cursor.fetchall():
                print("\t".join(item))
        elif self.Search.uuid != False and self.Search.name == False:
            select = ("SELECT Uuid, Parent FROM PPID_CONTENT WHERE Uuid='%s'" %(self.Search.uuid))
            self.cursor.execute(select)
            print("%s\t%s\t%s\t%s\t%s" %('Uuid', 'Path', 'Name', 'Commmit', 'Parent'))
            for item in self.cursor.fetchall():
                print("\t".join(item))
        else:
            print("'--uuid' or '--name' two parameters must be have one")
        
        self.Close()

    def Tree(self):
        self.Init()
        if self.Search.uuid != False or self.Search.name != False:
            select = ("SELECT Uuid, Parent FROM PPID_CONTENT WHERE Uuid='%s' OR Name='%s'" %(self.Search.uuid, self.Search.name))
            self.cursor.execute(select)
            select_node = self.cursor.fetchone()

            if select_node:
                parent_node_list = collections.OrderedDict()
                child_node_list = collections.OrderedDict()
                select_child = select_node[0]
                select_parent = select_node[1]

                if select_node[1] == "...":
                    child_level = 0
                    tag = True
                    while tag:
                        self.cursor.execute("SELECT Uuid, Parent FROM PPID_CONTENT WHERE Parent='%s'" %(select_child))
                        if self.cursor.fetchone():
                            child_level += 1
                            child_node_list[child_level] = list(self.cursor.fetchone())[0]
                            select_child = self.cursor.fetchone()[0]
                            tag = True
                        else:
                            tag = False
                else:
                    child_level = 0
                    parent_level = 0
                    child_tag = True
                    parent_tag = True

                    while child_tag:
                        self.cursor.execute("SELECT Uuid, Parent FROM PPID_CONTENT WHERE Parent='%s'" %(select_child))
                        child_node = self.cursor.fetchone()
                        if child_node:
                            child_level += 1
                            child_node_list[child_level] = child_node[0]
                            select_child = child_node[0]
                            child_tag = True
                        else:
                            child_tag = False
                    
                    while parent_tag:
                        self.cursor.execute("SELECT Uuid, Parent FROM PPID_CONTENT WHERE Uuid='%s'" %(select_parent))
                        parent_node = self.cursor.fetchone()
                        if parent_node:
                            parent_level += 1
                            parent_node_list[parent_level] = parent_node[0]
                            select_parent = parent_node[1]
                            parent_tag = True
                        else:
                            parent_tag = False         
            else:
                print("Can't find record about your input")

            
            if parent_node_list == collections.OrderedDict():
                pass

        self.Close()




    