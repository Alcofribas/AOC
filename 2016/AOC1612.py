#!/usr/bin/python2

# rank:

# usage: python AOC1612.py < AOC1612_input.txt > AOC1612_output.txt

from collections import defaultdict
import re
import sys

# read data
instructions = [line.strip().split(' ') for line in sys.stdin]

def day12(a,b,c,d):

    def readarg(x):
        if re.match(r'[abcd]',x):
            return regs[x]
        else:
            return int(x)

    # quicker alternative for readarg
    # def readarg(x):
    # try:
    #     return int(x)
    # except:
    #     return regs[x]

    # nice: use defaultdict to handle missing values in dict!
    ip = 0
    regs = {'a': a,
            'b': b,
            'c': c,
            'd': d }
    EOF = len(instructions)

    # execute instructions
    while ip < EOF:
        inst = instructions[ip]
        if inst[0] == 'cpy':
            regs[inst[2]] = readarg(inst[1])
        elif inst[0] == 'inc':
            regs[inst[1]] += 1
        elif inst[0] == 'dec':
            regs[inst[1]] -= 1
        elif inst[0] == 'jnz':
            if readarg(inst[1]) != 0:
                ip += readarg(inst[2])-1
        ip += 1

    return regs

if __name__ == "__main__":

    print 'Answer to Part 1: %d' % day12(0, 0, 0, 0)['a']

    print 'Answer to Part 2: %d' % day12(0, 0, 1, 0)['a']
