#!/usr/bin/awk

# AOC 2016 Day 9 Model Solution
# https://www.reddit.com/r/adventofcode/comments/5hbygy/2016_day_9_solutions/daz4c16/

# find out how to run this from command line

function dec(str, total, code, ix, len, rep, tmp) {
    total = 0
    while (match(str, /\([[:digit:]]+x[[:digit:]]+\)/)) {
        code = substr(str, RSTART+1, RLENGTH-2)
        ix = index(code, "x")
        len = 0 + substr(code, 1, ix-1)
        rep = 0 + substr(code, ix+1)

        total += RSTART-1 + rep * dec(substr(str, RSTART+RLENGTH, len))
        str = substr(str, RSTART+RLENGTH+len)
    }
    total += length(str)
    return total
}

{ print dec($0) }
