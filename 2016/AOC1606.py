#!/usr/bin/python

import operator
import os
import re
import sys

day = 6

def updateCounts(mess):
    # sys.stderr.write("Processing message: %s" % mess)
    # sys.stderr.write('\n')
    for i,letter in enumerate(mess):
        # sys.stderr.write("Letter %02d: %s" % (i, letter))
        # sys.stderr.write('\n')
        if letter in freqs[i]:
            freqs[i][letter] += 1
        else:
            freqs[i][letter] = 1
    sys.stderr.write(str(freqs))
    sys.stderr.write('\n')

def denoisedMessage():
    return ''.join([min(x.iteritems(), key=operator.itemgetter(1))[0] for x in freqs])

# Arbeitsverzeichnis setzen
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# load data
infile = open('AOC16%02d_input.txt' % day)
messages = [line.rstrip('\n') for line in infile]
infile.close()

orig_stdout = sys.stdout
outfile = open("AOC16%02d_output.txt" % day,"w")
sys.stdout = outfile

freqs=[]

for i in range(len(messages[0])):
    freqs.append({})

for message in messages:
    updateCounts(message)

print "Message: %s" % (denoisedMessage())

sys.stdout = orig_stdout
outfile.close()
