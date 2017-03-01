#!/usr/bin/python

import sys

for line in sys.stdin:
    seq,value = line.strip().split("\t")
    tokens = seq.split(' ')
    token1 = tokens[0].strip() + ' ' + tokens[1].strip()
    print"{0}\t{1}".format(token1,value)
