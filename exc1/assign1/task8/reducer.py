#!/usr/bin/python

import sys
i = 0
for line in sys.stdin:
    if i < 1:
        name,avg=line.strip().split(" ")
        name = name.strip()
        print (name)
        i += 1
