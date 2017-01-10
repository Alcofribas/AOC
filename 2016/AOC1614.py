"""
AOC1614 Puzzle: One-Time Pad
"""
#!/usr/bin/python2

# usage: AOC1614.py < AOC1614_input.txt

# rank: ---

from collections import defaultdict
from hashlib import md5
import re
import sys

def day20(salt,f):

    # set variables
    triples = defaultdict(list)
    solved1 = False
    keys = []
    index = 0

    def stretch(x,f):
        tmp = x
        for i in range(f):
            tmp = md5(tmp).hexdigest()
        return tmp

    while True:
        hash = stretch(salt+str(index),f)

        # quintle check
        match = re.search(r'(.)\1\1\1\1',hash)
        if match:
            char = hash[match.start()]
            for cand in triples[char]:
                print "%d: Key #%d %s found at index %d" % (index,len(keys),cand[1],cand[0])
                if cand[1] not in [x[1] for x in keys]:
                    keys.append(cand)
                if len(keys) == 64:
                    return cand[0]

        # triple check
        match = re.search(r'(.)\1\1',hash)
        if match:
            triples[hash[match.start()]].append((index,hash))
            print "Triple found in %s at index %d" % (hash,index)

        # remove "outdated candidates"
        for x in triples.keys():
            triples[x] = [y for y in triples[x] if y[0]>(index-1000)]

        index += 1

salt = 'cuanljph'
# print "Answer Part 1: %d" % day20(salt,1)
print "Answer Part 2: %d" % day20(salt,2017)
