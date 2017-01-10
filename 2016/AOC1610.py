#!/usr/bin/python2

# rank: 329/312

# usage: AOC1610.py < AOC1610_input.txt > AOC1610_output.txt

import os
import re
import sys

def day10(data):

    bots = {}
    out = {}

    t = [0,0]
    v = [0,0]

    solution1 = None
    solution2 = None

    data2 = []
    act = []

    def findInstr(dat, bot):
        for i,line in enumerate(dat):
            if re.search(' ' + bot + ' gives',line):
                return i
        return None

    def give(t,i,v):
        if t=='bot':
            if i not in bots:
                bots[i]=[]
            else:
                act.append(i)
            bots[i].append(v)
        else:
            if i not in out:
                out[i]=[v]
            else:
                out[i].append(v)

    # initbots
    while data:
        line = data.pop()
        if re.search('goes to',line):
            v, b = (x for x in re.search('value (\d+) goes to bot (\d+)',line).groups(1))
            if b not in bots:
                bots[b] = []
            else:
                act = [b] + act
            bots[b].append(v)
        else:
            data2.append(line)

    print bots
    print act

    # handlechips
    while len(act)>0:
        actbot = act.pop()
        idx = findInstr(data2, actbot)
        if idx is None:
            continue
        instr = data2[idx]
        data2 = data2[:idx]+data2[idx+1:]
        val = sorted(bots[actbot],key=int)
        if val == ['17','61']:
            solution1 = actbot
        t = [0,0]
        nr = [0,0]
        t[0],nr[0],t[1],nr[1] = re.search(' '+actbot+' gives low to (output|bot) (\d+) and high to (output|bot) (\d+)',instr).groups(1)
        give(t[0],nr[0],val[0])
        give(t[1],nr[1],val[1])
        print act

    print out
    print "Robot comparing 17 and 61: %s" % solution1
    print "Product of values in outputs 0,1,2: %d" % (int(out['0'][0])*int(out['1'][0])*int(out['2'][0]))
    # solution output
    # print "Length of decompressed file Part 2: %s" % data

if __name__ == "__main__":

    instr = [line.rstrip('\n') for line in sys.stdin]
    day10(instr)
