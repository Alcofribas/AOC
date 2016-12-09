#!/usr/bin/python2

# rank: 506/293

# to get a more elegant solution, parse input character-wise!

import os
import re
import sys

day = 9

# set working dir
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# load data
infile = open('AOC16%02d_input.txt' % day)
data = [line.rstrip('\n').split() for line in infile][0][0]
infile.close()

# decompression algorithms

def day9a(d):
    bracket = re.search(r'\((\d+)x(\d+)\)', d[0:])
    if not bracket:
        return len(d)
    pos = bracket.start(0)
    sz = int(bracket.group(1))
    rpt = int(bracket.group(2))
    i = pos + len(bracket.group())
    return len(d[:pos]) + len(d[i:i+sz]) * rpt + day9a(d[i+sz:])

def day9b(d):
    bracket = re.search(r'\((\d+)x(\d+)\)', d[0:])
    if not bracket:
        return len(d)
    pos = bracket.start(0)
    sz = int(bracket.group(1))
    rpt = int(bracket.group(2))
    i = pos + len(bracket.group())
    return len(d[:pos]) + day9b(d[i:i+sz]) * rpt + day9b(d[i+sz:])

# solution output
print "Length of decompressed file Part 1: %d" % (day9a(data))
print "Length of decompressed file Part 2: %d" % (day9b(data))
