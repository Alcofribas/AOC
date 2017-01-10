"""
AOC1620 Puzzle: Firewall Rules
"""
#!/usr/bin/python2

# usage: AOC1620.py < AOC1620_input.txt

# rank: 519/494

import sys

def day20(blocked):

    # set variables
    highest = 0
    solved1 = False
    changed = True
    blocked = sorted(blocked,key=lambda x: x[0])
    allowed = []

    # logic
    for iprange in blocked:
        # print iprange, highest
        lower, upper = iprange
        if (lower>highest):
            # print "Found allowed: %s" % (' '.join(map(str,range(highest,lower))))
            allowed += range(highest,lower)
            if not solved1:
                print "Answer Part 1: %d" % (min(allowed))
                solved1 = True
        highest = max(highest,upper+1)
    allowed += range(highest,4294967296)
    print "Answer Part 2: %d" % len(allowed)
blocklist = [map(int,line.strip().split('-')) for line in sys.stdin]
day20(blocklist)
