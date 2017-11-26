#!/usr/bin/env python
import os, re, sys
from socket import gethostname
pwd = os.getcwd()
#pwd = sys.argv[1]
homedir = os.path.expanduser('~')
pwd = pwd.replace(homedir, '~', 1)

sp = pwd.split('/')
#from IPython import embed
#embed()

def only_one(sub, arr):
	cnt = 0
	#print (sub, arr)
	for f in arr:
		if f.startswith(sub): cnt += 1
		if cnt > 1: return False
	if cnt == 1: return True
	return False

for i, j in enumerate(re.finditer(r"/",pwd)):
	if j.start() == 0: continue
	curr_path = os.path.expanduser(pwd[:j.start()])
	ls = os.listdir(curr_path)
	s = ''
	for k, c in enumerate(sp[i+1]):
		s += c
		if only_one(s, ls): break
	sp[i+1] = s
	#print(curr_path)
	#print(s)
	#print('-----------------')

path = '/'.join(sp)
print(path)
