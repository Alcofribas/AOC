"""
AOC1615 Puzzle: Timing is Everything
"""
#!/usr/bin/python2

# usage: AOC1615.py < AOC1615_input.txt

# rank: ---

import re
import sys

def day15(conf):

    # set variables
    state = [conf[x][1]+x+1 for x in range(len(conf))]
    time = 0
    discs = range(len(state))

    while sum(state) != 0:
        time += 1
        # print state
        state = [(state[x] + 1) % conf[x][0] for x in discs]
    return time

setup = [list(re.search(r'Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).',line).groups()) for line in sys.stdin]
setup = [[int(setup[x][1]),int(setup[x][3])] for x in range(len(setup))]
print "Answer Part 1: %d" % day15(setup)
# add disc with 11 positions, starting with state 0
setup.append([11,0])
print "Answer Part 2: %d" % day15(setup)
