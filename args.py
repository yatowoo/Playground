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

parser = ArgumentParser()
# Positional arguments
parser.add_argument("SAIMOE_YEAR",help="Year of NGA Kancolle Saimoe", type=int, choices=list(range(2014,2019)))
parser.add_argument("SAIMOE_STAGE",help="Stage of NGA Kancolle Saimoe", choices=['group_stage', 'repechage', '1v1'])
# Optional arguments
parser.add_argument("-g", "--group", help="Group of NGA Kancolle Saimoe : A..Z, 32/16/8/4-A..Z (for 1v1), SA..SZ (for Shinkai)")
parser.add_argument("--local", help="Do not update thread data, analysis with existed local files", action="store_true", default=False)
parser.add_argument("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_argument("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
print(args)