#!/usr/bin/python2

# rank: 525/474

# usage: python AOC1616.py < AOC1616_input.txt > AOC1616_output.txt

import sys

def day16(seed,space):

    # variables setup
    fill = seed
    notx = {'0':'1','1':'0'}
    checkgen = {'00':'1','01':'0','10':'0','11':'1'}

    # helper functions
    def expand(x):
        return x + '0' + ''.join([notx[a] for a in x])[::-1]

    def checksum(x):
        tmp = ''.join([checkgen[x[s*2:(s+1)*2]] for s in range(len(x)/2)])
        if len(tmp) % 2 == 0:
            return checksum(tmp)
        else:
            return tmp

    # logic
    # print "Expand seed..."
    while len(fill) < space:
        fill = expand(fill)
    # print "Generate checksum..."
    return checksum(fill[:space])

if __name__ == "__main__":

    # read data
    seed = [line.strip() for line in sys.stdin][0]
    print 'Answer to Part 1: %s' % day16(seed, 272)
    print 'Answer to Part 2: %s' % day16(seed, 35651584)
    # print 'Answer to Part 2: %d' % day13()
