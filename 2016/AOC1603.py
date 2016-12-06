#!/usr/bin/python

import os
import sys

# Arbeitsverzeichnis setzen
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# load data
infile = open('AOC1603_input.txt')
tri = [line.rstrip('\n').lstrip(' ').split() for line in infile]
# debug: print tri
infile.close()

# check
output = open("AOC1603_output.txt","w")
orig_stdout = sys.stdout
sys.stdout = output

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

# write travel protocol
#
# output.writelines([str(x)+"\n" for x in path])
sys.stdout = orig_stdout
output.close()
