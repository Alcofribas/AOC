#!/usr/bin/python2

# not the most elegant solution, but works

import os
import re
import sys

day = 8

# initialize screen
w, h = 50, 6
screen = [[0 for x in range(w)] for y in range(h)]

def rotate(pars):
    t,i,o = pars[0], int(re.sub(r'(x|y)=','',pars[1])),int(pars[3])
    if t=='row':
        screen[i]=screen[i][-o:]+screen[i][:-o]
    else:
        # rotate column
        col=[screen[y][i] for y in range(h)]
        rotcol = col[-o:]+col[:-o]
        for n in range(h):
            screen[n][i]=rotcol[n]

def rect(pars):
    c,r = [int(x) for x in pars[0].split('x')]
    for x in range(c):
        for y in range(r):
            screen[y][x] = 1

def showpad():
    for i in range(h):
        print ''.join([re.sub('0','.',re.sub('1','#',str(x))) for x in screen[i]])
    print '-------------------'

# set working dir
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# load data
infile = open('AOC16%02d_input.txt' % day)
coms = [line.rstrip('\n').split() for line in infile]
infile.close()

orig_stdout = sys.stdout
outfile = open("AOC16%02d_output.txt" % day,"w")
sys.stdout = outfile

# run commands
for com in coms:
    fun = com[0]
    globals()[fun](com[1:])
    showpad()

# solution output
lit = sum([sum(x) for x in screen])
print "Number of lit pixels: %d" % (lit)

sys.stdout = orig_stdout
outfile.close()
