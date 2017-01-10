"""
AOC1619 Puzzle: An Elephant Named Joseph
Variant of the Josephus problem
see: https://en.wikipedia.org/wiki/Josephus_problem
see: https://www.reddit.com/r/adventofcode/comments/5j4lp1/2016_day_19_solutions/
"""
#!/usr/bin/python2

# usage: python AOC1619.py

class Node:
  def __init__(self,id):
    self.id  = id
    self.nxt = None
    self.prv = None

  def delete(self):
    self.prv.nxt = self.nxt
    self.nxt.prv = self.prv

def solve(n):
  l = map(Node, xrange(n))
  for i in xrange(n):
    l[i].nxt = l[(i+1)%n]
    l[i].prv = l[(i-1)%n]

  start = l[0]
  mid   = l[n/2]

  for i in xrange(n-1):
    mid.delete()
    mid = mid.nxt
    if (n-i)%2==1: mid = mid.nxt
    start = start.nxt

  return start.id+1

print "Answer Part 2: %d" % solve(3012210)
