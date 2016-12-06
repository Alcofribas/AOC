#!/usr/bin/python

from operator import add
import os
import sys

# Arbeitsverzeichnis setzen
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

movements = [[0,-1],[1,0],[0,1],[-1,0]]

# load directions
dirFile = open("AOC1601_input.txt")
directions = dirFile.read().split(', ')
print directions
dirFile.close()

# walk!
relPos = [0,0]
curDir = 0
path = [relPos]
end = False

for dir in directions:
    if dir[0] == 'L':
        curDir += -1+(curDir==0)*4
    else:
        curDir += 1-(curDir==3)*4
    delta = movements[curDir]
    for step in range(int(dir[1:])):
        relPos = map(add, relPos, delta)
        if relPos not in path:
            path.append(relPos)
        else:
            path.append(relPos)
            end = True
            break
    if end:
        break

# calculate distance
dist = sum([abs(x) for x in relPos])
print dist

# write travel protocol
output = open("AOC1601_output.txt","w")
output.writelines([str(x)+"\n" for x in path])
output.close()
