#!usr/bin/python
#coding: utf-8
import argparse
import os
import datetime
import sys
import getpass
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--time", action="store_true", help="show actual time")
parser.add_argument("-d", "--date", action="store_true", help="show actual date")
parser.add_argument("-T", "--tree", action="store_true", help="show the list of files in a directory")
parser.add_argument("-l", "--login", action="store_true", help="show the current user")
parser.add_argument("-v", "--version", action="store_true", help="show interpreter Python version")
args=parser.parse_args()
date=datetime.datetime.now()
time=date.time()
date=date.date()
tree=os.listdir(os.getcwd())
version=sys.version
login=getpass.getuser()
if args.time:
    print 'Tекущее время: {}'.format(time)
elif args.date:
    print 'Текущая дата: {}'.format(date)
elif args.tree:
    print 'Список файлов в директории: {}'.format(tree)
elif args.version:
    print 'Версия итерпритатора Python: {}'.format(version)
elif args.login:
    print 'Текущий пользователь: {}'.format (login)
