#!/usr/bin/python

import hashlib
import os
import re
import sys

def md5hex(str):
    return hashlib.md5(str).hexdigest()

def codeletter(hexhash):
    if re.match('00000', hexhash) != None:
        return (int(hexhash[5],16), hexhash[6])
    else:
        return (None,'')

# Arbeitsverzeichnis setzen
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# load data
infile = open('AOC1605_input.txt')
doorIDs = [line.rstrip('\n') for line in infile]
infile.close()

# print roomlist

orig_stdout = sys.stdout
outfile = open("AOC1605_output.txt","w")
sys.stdout = outfile

for id in doorIDs:
    print "---------------"
    passcode = '--------'
    idx = 0
    while '-' in passcode:
        hashbase = id+str(idx)
        tmp = md5hex(hashbase)
        nextpos, nextlet = codeletter(tmp)
        if (nextpos in range(8)):
            if passcode[nextpos] == '-':
                tmp2 = list(passcode)
                tmp2[nextpos] = nextlet
                passcode = ''.join(tmp2)
        idx += 1
        if nextlet != '':
            print "%s--- %s --- %s --- %s" % (tmp, nextlet, passcode, hashbase)
    print "Door ID: %s --- Code: %s" % (id, passcode)

# write travel protocol
#
# output.writelines([str(x)+"\n" for x in path])
sys.stdout = orig_stdout
outfile.close()
