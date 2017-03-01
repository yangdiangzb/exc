#!/usr/bin/python

import sys
import math

prev_seq= ''
value_list = ''
for line in sys.stdin:
    seq,count = line.strip().split("\t")

    if seq != prev_seq:
        if prev_seq:
            value_total = 0.0
            num_total = 0.0
            values = value_list.split()
            for value in values:
                value_total +=int(value)
            for value in values:
                par = int(value)/float(value_total)
                num_total += math.log(par,2) * (-1) * (par)
            print("{0} {1}".format(prev_seq,num_total))
        prev_seq,value_list = seq, count
    else:
        value_list = value_list  + ' ' + count
if prev_seq:
    value_total = 0.0
    num_total = 0.0
    values = value_list.split()
    for value in values:
        value_total +=int(value)
    for value in values:
        par = int(value)/float(value_total)
        num_total += math.log(par,2) * (-1) * (par)
    print("{0} {1}".format(prev_seq,num_total))
