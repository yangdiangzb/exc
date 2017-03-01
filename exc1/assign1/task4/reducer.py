#!/usr/bin/python

import sys

prev_seq = ""
value_total = 0
seq = ""
for line in sys.stdin:
    seq, value = line.strip().split("\t", 1)
    value = int(value)
    if seq != prev_seq:
        if prev_seq:
            print("{0}\t{1}".format(prev_seq,value_total))
        prev_seq, value_total = seq, value
    else:
        value_total += value

if prev_seq:
    print("{0}\t{1}".format(prev_seq,value_total))
