#!/usr/bin/python

# this code is currenntly solving part 2 of the puzzle

import os
import sys

# set working dir
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# load data
infile = open('AOC1603_input.txt')
tri = [line.rstrip('\n').lstrip(' ').split() for line in infile]
infile.close()

# redirect stdout to file
output = open("AOC1603_output.txt","w")
orig_stdout = sys.stdout
sys.stdout = output

# check triangles
valid = 0
for c in range(0,len(tri)-2,3):
    print c
    for r in [0,1,2]:
        t = sorted(map(int,[tri[c][r],tri[c+1][r],tri[c+2][r]]))
        if (t[0]+t[1])>t[2]:
            valid += 1
            print "%s ***" % t
        else:
            print "%s" % t

print "Number of valid triangles: %d" % valid

sys.stdout = orig_stdout
output.close()
