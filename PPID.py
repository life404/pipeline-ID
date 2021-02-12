#! /usr/bin/env python3

import os
import sys
import Search
import argparse
import sqlite3

def make_args():
    parse = argparse.ArgumentParser()
    parse.add_argument("-i", "--input", required=True, type=str, help="the path of research, could be directory or file (absoulte path)")
    parse.add_argument("-n", "--name", type=str, default=False, help="the alias of research, default is the uuid of research")
    parse.add_argument("-u", "--uuid", type=str, default=False, help="the unique identifier of Research, default is the code producted by uuid")
    parse.add_argument("-p", "--parent", type=str, default=False, help="the parent none of reseach")
    parse.add_argument("-c", "--commit", type=str, default=False, help="the commit of research")

    args = parse.parse_args()
    return args

def main():
    args = make_args()

    test = Search.Search(path=args.input, commit=args.commit, name=args.name, parent=args.parent, uuid=args.uuid)

    test.info()

if __name__ == "__main__":
    main()

    