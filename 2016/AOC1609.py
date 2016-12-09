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
compressed = [line.rstrip('\n').split() for line in infile][0][0]
infile.close()

orig_stdout = sys.stdout
outfile = open("AOC16%02d_output.txt" % day,"w")
sys.stdout = outfile

# decompression algorithms

def decompress1(data):
    decompressed = ''
    EOS = False
    while not EOS:
        nextmark = re.search('\((\d+)x(\d+)\)',data)
        if nextmark is not None:
            l,r = (int(x) for x in nextmark.groups(1))
            decompressed += data[:nextmark.start(1)-1]
            a = nextmark.end(2)+1
            c = len(data)
            b = a+l if (a+l)<=c else c
            if (b==c):
                EOS = True
            tmpdata = data[a:b]
            decompressed += tmpdata*r
            data = data[b:]
        else:
            decompressed += data
            EOS = True
    return decompressed

def decompress2(data):
    decomplen = 0
    EOS = False
    while not EOS:
        nextmark = re.search('\((\d+)x(\d+)\)',data)
        if nextmark is not None:
            l,r = (int(x) for x in nextmark.groups(1))
            decomplen += len(data[:nextmark.start(1)-1])
            a = nextmark.end(2)+1
            c = len(data)
            b = a+l if (a+l)<=c else c
            if (b==c):
                EOS = True
            tmpdata = data[a:b]
            decomplen += decompress2(tmpdata)*r
            data = data[b:]
        else:
            decomplen += len(data)
            EOS = True
    return decomplen

decompressed1 = decompress1(compressed)
decomplen2 = decompress2(compressed)

# solution output
print "Length of decompressed file Part 1: %d" % (len(decompressed1))
print "Length of decompressed file Part 2: %d" % (decomplen2)

sys.stdout = orig_stdout
outfile.close()
