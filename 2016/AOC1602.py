#!/usr/bin/python

import os
import sys

code = ""

# scheme for keypad definition: UDLR
moves = {"U": 0, "D": 1, "L": 2, "R": 3}

# where we end up when going in each direction from every key
keypad1 = { "1": "1412", "2": "2513", "3": "3623", "4": "1745", "5": "2846",
           "6": "3956", "7": "4778", "8": "5879", "9": "6989" }

keypad2 = { "1": "1311", "2": "2623", "3": "1724", "4": "4834", "5": "5556",
           "6": "2A57", "7": "3B68", "8": "4C79", "9": "9989", "A": "6AAB",
           "B": "7DAC", "C": "8CBC", "D": "BDDD" }

# keys to start with
pos1 = "5"
pos2 = "5"

# code initialization
code1 = ""
code2 = ""

# get instructions from front desk
infile = open("/home/oliver/Schreibtisch/AOC2016/AOC1602_input.txt")
instructions = infile.read()

# follow instructions
for move in instructions:
    # debug output:
    # print "Pos1: %s, Pos2: %s, Move: %s" % (pos1, pos2, move)
    if move != "\n":
        pos1 = keypad1[pos1][moves[move]]
        pos2 = keypad2[pos2][moves[move]]
    else:
        code1 += pos1
        code2 += pos2

print "Bathroom Codes: %s (Code 1) and %s (Code 2)" % (code1, code2)
