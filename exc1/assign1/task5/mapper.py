#!/usr/bin/python

import sys

for line in sys.stdin:
    seq,value = line.strip().split("\t")
    print "{0} {1}".format(value, seq)
