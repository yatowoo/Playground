#!/usr/bin/env python3

# Interact with shell

import os, subprocess

print('Test - interact with shell')
cmd = 'ls -a'

print('\n>>> os.sytem')
ret = os.system(cmd)

print('\n>>> os.popen')
ret = os.popen(cmd)
print(ret.read())

print('\n>>> subprocess.call')
ret = subprocess.call(cmd, shell=True)

print('\n>>> subprocess.popen')
ret = subprocess.Popen(cmd ,shell=True, stdout=subprocess.PIPE)
print(ret.stdout.read())