#! /usr/bin/env python3

import sqlite3
import os
import Search

class SQL():
    def __init__(self, Search):
        self.Search = Search
        self.sql_path = os.path.join(os.getcwd(), "PPID.db")

    def Init(self):
        self.cursor = sqlite3.connect(self.sql_path).cursor()
        create_tbl = "CREATE TABLE IF NOT EXIST PPID_CONTENT (uuid TEXT PRIMARY KEY, path TEXT, name TEXT, commit TEXT, parent TEXT)"
        self.cursor.execute(create_tbl)
        
    def Add(self):
        self.cursor.



    
