#!/usr/bin/python2

# rank:

# usage: python AOC1612.py < AOC1612_input.txt > AOC1612_output.txt

from collections import deque
import re
import sys

def day13(start,end):

    # variables setup
    maze = {}
    visited = {}
    shortest = []

    # helper functions
    def find_shortest_path(start,end,howwegothere,shortest):
        if not (shortest and len(howwegothere)>=shortest):
            if start == end:
                if len(howwegothere)<len(shortest):
                    shortest = howwegothere
            else:
                visited[start] = True
                howwegothere.append(start)
                x,y = start
                for dir in [(1,0),(0,1),(-1,0),(0,-1)]:
                    if get_block(x+dir[0],y+dir[1]) is not None:
                        find_shortest_path((x+dir[0],x+dir[1]),end,howwegothere,shortest)

    def get_block(x,y):
        # what is at (x,y)?
        if x<0 or y<0:
            return None
        if (x,y) not in maze:
            maze[(x,y)] = (len(re.sub('0','',bin(x*x+3*x+2*x*y+y+y*y+favnum)[2:])) % 2 == 0)
        return maze[(x,y)]

    # logic
    find_shortest_path(start,end,[],shortest)
    return shortest

if __name__ == "__main__":

    # read data
    favnum = int([line.strip() for line in sys.stdin][0])
    print 'Answer to Part 1: %d' % len(day13((1,1),(31,39)))
    # print 'Answer to Part 2: %d' % day13()
