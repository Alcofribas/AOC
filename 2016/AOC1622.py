"""
AOC1622 Puzzle: Grid Computing
"""
#!/usr/bin/python2

# usage: python AOC1622.py < AOC1622_input.txt

# rank: ---

import re
import sys

patterns = {
    r'swap letter (\w) with letter (\w)':'swap_letter',
    r'swap position (\d) with position (\d)':'swap_pos',
    r'rotate based on position (of) letter (\w)':'rotate_pos',
    r'rotate (\w+) (\d) steps?':'rotate_steps',
    r'move position (\d+) to position (\d+)':'move',
    r'reverse positions (\d+) through (\d+)':'reverse'
}

def day22(p,scramblist,unscr):

    def swap_letter(x,a,b):
        n,m = sorted([(re.search(z,x).start(), z) for z in [a,b]])
        return x[:n[0]]+m[1]+x[n[0]+1:m[0]]+n[1]+x[m[0]+1:]

    def swap_pos(x,a,b):
        a,b = int(a),int(b)
        n,m = x[a],x[b]
        return swap_letter(x,n,m)

    def move(x,a,b):
        a,b = int(a),int(b)
        if unscr:
            a,b = b,a
        c = x[a]
        tmp = x[:a]+x[a+1:]
        return tmp[:b]+c+tmp[b:]

    def rotate_pos(x,a,b):
        idx = re.search(b,x).start()
        if unscr:
            if idx % 2 == 0:
                rot = -(6-(idx+(idx==0)*8))/2
            else:
                rot = ( idx + 1 ) / 2
        else:
            rot = (1 + idx + (idx>3)*1) % len(x)
        return rotate_steps(x,'right',rot)

    def rotate_steps(x,a,b):
        b = int(b)
        if a == 'left':
            b = -b
        if unscr:
            b = -b
        return x[-b:]+x[:-b]

    def reverse(x,a,b):
        a,b = int(a),int(b)
        return x[:a]+x[a:b+1][::-1]+x[b+1:]

    for action in scramblist:
        # print p
        x = 0
        options = patterns.keys()
        while re.match(options[x],action) is None:
            x += 1
        # print action,x
        fun = patterns[options[x]]
        a, b = [re.match(options[x],action).group(y) for y in [1,2]]
        # print fun, a, b
        p = locals()[fun](p,a,b)

    return p

scramblist = [line.strip() for line in sys.stdin]

passw = 'abcdefgh'

print "Answer Part 1: %s" % day22(passw, scramblist, False)
# part 2:
# reverse actions themselves
# apply list of actions in reverse order
print "Answer Part 2: %s" % day22('fbgdceah',scramblist[::-1], True)
