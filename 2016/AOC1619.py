"""
AOC1619 Puzzle: An Elephant Named Joseph
Variant of the Josephus problem
see: https://en.wikipedia.org/wiki/Josephus_problem
"""
#!/usr/bin/python2

# usage: python AOC1619.py

# rank: ---

import re
import sys

def day19(elves):

    def highest_bit(n):
        return 2**(len(bin(n))-3)

    def get_winner(n):
        l = n - highest_bit(n)
        return 2 * l + 1

    return get_winner(elves)

elves = 3012210
print "Answer Part 1: %d" % day19(elves)
# print "Answer Part 2: %d" % day18(firstrow,400000,1)
