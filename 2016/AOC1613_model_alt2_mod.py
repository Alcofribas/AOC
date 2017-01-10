#!/usr/bin/python

# source: https://www.reddit.com/r/adventofcode/comments/5i1q0h/2016_day_13_solutions/db4qgz8/

# list comprehension warrior!
# assumes that you can't go on forever (no break condition in maze walkthrough!)

# solution of modified version not correct!

favnum = 1358
start = (1,1)

# frontier format: x,y,pathlen
frontier = [(start[0],start[1],0,[])]

# explored holds length of shortest path to each position visited as well as the path itself
explored = {}

def free(tup):
    num = tup[0] * tup[0] + 3 * tup[0] + 2 * tup[0] * tup[1] +tup[1] + tup[1] * tup[1] + favnum
    return bin(num)[2:].count("1") % 2 == 0 and tup[0] >= 0 and tup[1] >= 0

def get_next(tup):
    cand = [(0,1), (0,-1), (1,0), (-1,0)]
    return [(x[0] + tup[0], x[1] + tup[1], tup[2] + 1, tup[3]+[(x[0] + tup[0],x[1] + tup[1])]) for x in cand if free((x[0] + tup[0], x[1] + tup[1]))]

while len(frontier) > 0:
    new = frontier.pop()
    if ((new[0],new[1]) not in explored) or (new[2] < explored[(new[0], new[1])][0]):
        explored[(new[0], new[1])] = (new[2],new[3])
    frontier += [x for x in get_next(new) if not (x[0], x[1]) in explored or explored[(x[0], x[1])][0] > x[3]]
    print explored

print explored[(31,39)], len([explored[x] for x in explored.keys() if explored[x][0] <= 50])
