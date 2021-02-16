#! /usr/bin/env python3

import os
import sys
from Search import *
import argparse
from SQL import *

def make_args():
    parse = argparse.ArgumentParser(prog="PPID")
    subparse = parse.add_subparsers(help="The subcommand of `ADD`, `UPDATE`, `REBUILD`")

    parse_add = subparse.add_parser('add', help="The subcommand of `ADD A NEW ITEM`")
    parse_add.add_argument("-i", "--input", required=True, type=str, help="the path of research, could be directory or file (absoulte path)")
    parse_add.add_argument("-n", "--name", type=str, default=False, help="the alias of research, default is the uuid of research")
    parse_add.add_argument("-u", "--uuid", type=str, default=False, help="the unique identifier of Research, default is the code producted by uuid")
    parse_add.add_argument("-p", "--parent", type=str, default=False, help="the parent none of reseach")
    parse_add.add_argument("-c", "--commit", type=str, default=False, help="the commit of research")
    parse_add.add_argument("-d", "--db", type=str, default="PPID.db", help="The datebase name of PPID")
    parse_add.set_defaults(func=Add_item)

    parse_update = subparse.add_parser('update', help="The subcommand of `UPDATE A ITEM`")
    parse_update.add_argument("--update", type=str, default=False, help="Update the content, shoud be used in condition `--uuid` were be specified manually")
    parse_update.add_argument("-u", "--uuid", type=str, default=False, help="the unique identifier of Research, default is the code producted by uuid")
    parse_update.add_argument("-d", "--db", type=str, default="PPID.db", help="The datebase name of PPID")
    parse_update.set_defaults(func=Update_item)

    parse_remove = subparse.add_parser('remove', help="The subcommand of `REBUILD`")
    parse_remove.add_argument("--reset", type=str, default=False, help="Remove the old database and rebuild a new one")
    parse_remove.add_argument("-d", "--db", type=str, default="PPID.db", help="The datebase name of PPID")
    parse_remove.set_defaults(func=Remove_db)

    parse_print = subparse.add_parser("print", help="The subcommand of `PRINT`")
    parse_print.add_argument("-l", "--level", default=1, type=int, help="The show level of tree format")
    parse_print.add_argument("-u", "--uuid", type=str, default=False, help="the unique identifier of Research, default is the code producted by uuid")
    parse_print.add_argument("-n", "--name", type=str, default=False, help="the alias of research, default is the uuid of research")
    parse_print.add_argument("-d", "--db", type=str, default="PPID.db", help="The datebase name of PPID")
    parse_print.set_defaults(func=Print_item)

    args = parse.parse_args()
    return args

def Add_item(args):
    search = Search()
    search.ADD(path=args.input, commit=args.commit, name=args.name, parent=args.parent, uuid=args.uuid)
    database = SQL(Search=search, dbname=args.db)
    database.Add()

def Update_item(args):
    if args.update:
        if args.uuid:
            search = Search()
            search.UPDATE(uuid=args.uuid, update=args.update)
            database = SQL(Search=search, dbname=args.db)
            database.Update()
        else:
            print("In 'UPDATE' mode, `--update` and `--uuid` two parameters were required")
    else:
        pass    

def Remove_db(args):
    search = Search()
    database = SQL(Search=search, dbname=args.db)
    database.Remove()

def Print_item(args):
    if args.uuid or args.name:
        search = Search()
        search.PRINT(uuid=args.uuid, name=args.name)
        database = SQL(Search=search, dbname=args.db)
        database.Select(args.level)
    else:
        print("'--uuid' or '--name' two parameters must be have one")

def main():
    args = make_args()
    args.func(args)



if __name__ == "__main__":
    main()

    