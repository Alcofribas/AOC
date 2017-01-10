"""
AOC1618 Puzzle: Like A Rogue
"""
#!/usr/bin/python2

# usage: AOC1618_input.py < AOC1618_input.txt

# rank: ---

import re
import sys

def day18(firstrow,n,p):

    # set variables
    floor = [firstrow]
    width = len(firstrow)

    def tile_type(lcr):
        if re.match(r'(\^.\.|\..\^)',lcr):
            return '^'
        else:
            return '.'

    for row in range(n-1):
        newrow= ''
        for i in range(width):
            if i == 0:
                newrow += tile_type('.'+floor[row][i:i+2])
            elif i == width-1:
                newrow += tile_type(floor[row][i-1:i+1]+'.')
            else:
                newrow += tile_type(floor[row][i-1:i+2])
        floor.append(newrow)
    # for i,y in enumerate(floor):
        # print "%02d %s" % (i,floor[i])
    if p == 1:
        # print [x.count('.') for x in floor]
        return sum([x.count('.') for x in floor])

firstrow = [line.strip() for line in sys.stdin][0]
numrows = 40
print "Answer Part 1: %d" % day18(firstrow,numrows,1)
print "Answer Part 2: %d" % day18(firstrow,400000,1)
# add disc with 11 positions, starting with state 0
# setup.append([11,0])
# print "Answer Part 2: %d" % day15(setup)
