#!/usr/bin/env python3
#coding=utf-8

# Practice for argparse
# Definition
#   ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
# Positional & optional(-)
# Option: 'short', 'long', help, type, default, choices, action
# Action: store[_const/true/false], append[_const], count, help, version
# Nargs: [N]/?/+/*
# Type: built-in, argparse.FileType('r/w...')
#   class argparse.FileType(mode='r', bufsize=-1, encoding=None, errors=None)
# Dest: var for storage in parser
# Metvar: alternative var for storage

import sys
import argparse

print(sys.argv)

from argparse import ArgumentParser

parser = ArgumentParser(description='Practice for module argparse')
# Positional arguments
parser.add_argument("YEAR",help="Year for test", type=int, choices=list(range(2014,2019)))
# Optional arguments
parser.add_argument("--local", help="Do not update thread data, analysis with existed local files", action="store_true", default=False)
parser.add_argument("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_argument("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
parser.add_argument('-i','--info',nargs='+', default=['2018', '1v1', 'A'])

print(parser.parse_args())