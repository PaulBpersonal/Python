import glob
import os
import datetime
 
rootdir = '//192.168.10.50/upload/'
out = 'C:/Users/Paul/Desktop/convert project/.vscode/IUAR.txt'
time = datetime.datetime.now()

print('In Use and Received as of:', file=open(out, "a"))
print(time, file=open(out, "a"))

print('\nIN-USE', file=open(out, "a"))

for inuse in glob.glob(f'{rootdir}/*/**/in-use/***', recursive=True):
    inp = inuse[24:]
    
    print(inp, file=open(out, "a"))

print('\nRECEIVED', file=open(out, "a"))

for rece in glob.glob(f'{rootdir}/*/**/received/***', recursive=True):
    rep = rece[24:]
    print(rep, file=open(out, "a"))

print('\r\n', file=open(out, "a"))

print('Complete')