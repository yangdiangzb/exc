#!/usr/bin/python

import sys
i = 0
for line in sys.stdin:
    if i < 20:
        value,seq = line.strip().split(" ",1)
        value = int(value)
        print "{0} {1}".format(value, seq)
        i = i + 1
