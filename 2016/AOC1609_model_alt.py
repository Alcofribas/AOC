# AOC 2016 day 9

# model solution
# taken from: https://www.reddit.com/r/adventofcode/comments/5hbygy/2016_day_9_solutions/daz2bou/

# use generators!
# use try/except as fast way of avoiding explicit workarounds

import re
from itertools import *
from sys import stdin

nums = re.compile(r'(\d+)')
text = stdin.read()

notLeft = lambda c : c != '('
notRight = lambda c : c != ')'

def decompress(gen):
    count = 0
    try:
        while True:
            count += len(list(takewhile(notLeft, gen)))
            marker = ''.join(takewhile(notRight, gen))
            [numChars, numRepeat] = map(int, nums.findall(marker))
            count += decompress(islice(gen, numChars)) * numRepeat
    except:
        return count
print decompress(iter(text))

# solution output
print "Length of decompressed file Part 1: %d" % (day9a(data))
print "Length of decompressed file Part 2: %d" % (day9b(data))
