#!/usr/bin/python2

# not the most elegant solution, but works

import os
import re
import sys

day = 7

def parseIP(ip):
    fragments = re.sub(r'(\[|\])',' ',ip).split()
    hyper = False
    result = ''
    for frag in fragments:
        result += str(hasTLSPattern(frag)+(2*hyper))
        hyper = not hyper
    return result

def supportsSSL(ip):
    fragments = re.sub(r'(\[|\])',' ',ip).split()
    hyper = False
    ins = []
    outs = []
    for frag in fragments:
        res = detectSSLPatterns(frag)
        if res is not None:
            if hyper:
                ins = ins+res
            else:
                # for matches outside brackets reverse char order
                outs = outs+[(y,x) for (x,y) in res]
        hyper = not hyper
    return len(set.intersection(set(ins), set(outs))) > 0

def hasTLSPattern(frag):
    # negative lookahead to exclude AAAA patterns
    return (re.search(r'(.)(?!\1)(.)\2\1',frag) is not None)

def detectSSLPatterns(frag):
    # lookahead assertion to include overlapping matches
    return re.findall(r'(?=(.)(?!\1)(.)\1)',frag)

def supportsTLS(ip):
    par = parseIP(ip)
    print ip, par
    return (re.search('3',par) is None) and (re.search('1',par) is not None)

# Arbeitsverzeichnis setzen
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# load data
infile = open('AOC16%02d_input.txt' % day)
ips = [line.rstrip('\n') for line in infile]
infile.close()

orig_stdout = sys.stdout
outfile = open("AOC16%02d_output.txt" % day,"w")
sys.stdout = outfile

# evaluate IPs
tls = [ip for ip in ips if supportsTLS(ip)]
ssl = [ip for ip in ips if supportsSSL(ip)]

# solution output
print "Number of IPs supporting TLS: %d" % (len(tls))
print "Number of IPs supporting SSL: %d" % (len(ssl))

sys.stdout = orig_stdout
outfile.close()
