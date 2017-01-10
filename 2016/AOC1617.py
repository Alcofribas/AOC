#!/usr/bin/python2

# rank: ---

# usage: python AOC1617.py > AOC1617_output.txt

from hashlib import md5
import re
import sys

def day17(passcode):

    # variables setup
    start = (0,0)
    frontier = [(start[0],start[1],'')]
    dirs = 'UDLR'
    # explored holds length of shortest path to each position visited as well as the path itself
    solved1 = False

    # helper functions
    def current_doors(state,passcode):
        doors = md5(passcode+state[2]).hexdigest()[:4]
        doors = re.sub(r'[0-9a]','0',doors)
        doors = re.sub(r'[^0]','1',doors)
        if state[0]==0:
            doors=doors[:2]+'0'+doors[3]
        else:
            if state[0]==3:
                doors=doors[:3]+'0'
        if state[1]==0:
            doors='0'+doors[1:]
        else:
            if state[1]==3:
                doors=doors[0]+'0'+doors[2:]
        return doors

    def get_next(state,passcode):
        cand = [(0,-1), (0,1), (-1,0), (1,0)]
        doors = current_doors(state,passcode)
        return [(state[0]+cand[x][0],state[1]+cand[x][1],state[2]+dirs[x]) for x in range(4) if doors[x]=='1']

    while len(frontier) > 0:
        new = frontier.pop()
        # print new
        if (new[0],new[1])!=(3,3):
            frontier = get_next(new,passcode) + frontier
        else:
            longest = len(new[2])
            if not solved1:
                print 'Answer to Part 1: %s' % new[2]
                solved1 = True
    print 'Answer to Part 2: %d' % longest

if __name__ == "__main__":

    # read data
    passcode = 'ioramepc'
    day17(passcode)
