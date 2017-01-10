#!/usr/bin/python2

from collections import defaultdict
import re
import sys

def day10():

    instructions = [line.strip() for line in sys.stdin]

    # nice: use defaultdict to handle missing values in dict!
    bots = defaultdict(list)
    outputs = defaultdict(list)
    which = [0,0]
    to = [0,0]

    # nice idea: precompiled regex!
    reg1 = r'value (\d+) goes to bot (\d+)'
    reg2 = r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)'

    # nice: just go through every instruction and see if it can (already) be processed
    i = 0
    while len(instructions) > 0:
        if i >= len(instructions):
            i = 0
        instruction = instructions[i]

        if re.match(reg1, instruction):
            # value command
            val, bot = map(int, re.findall(reg1, instruction)[0])
            bots[bot].append(val)
            del instructions[i]
        else:
            # give command
            bot, which[0], to[0], which[1], to[1] = re.findall(reg2, instruction)[0]
            bot, to[0], to[1] = int(bot), int(to[0]), int(to[1])
            if bot in bots and len(bots[bot]) == 2:
                val = sorted(bots[bot])
                if val[0] == 17 and val[-1] == 61:
                    print 'Answer to Part 1: %d' % bot
                bots[bot].remove(val[0])
                bots[bot].remove(val[-1])
                for j in [0,-1]:
                    if which[j] == 'bot':
                        bots[to[j]].append(val[j])
                    else:
                        outputs[to[j]].append(val[j])
                del instructions[i]
            else:
                i = (i + 1) % len(instructions)

    print 'Answer to Part 2: %d' % (outputs[0][0] * outputs[1][0] * outputs[2][0])

if __name__ == "__main__":
    day10()
