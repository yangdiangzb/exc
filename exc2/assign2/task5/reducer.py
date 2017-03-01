#!/usr/bin/python

import sys
import random

line_number = 0
line_total = 0
count = 0
for line in sys.stdin:
    keys=line.strip().split("\t")
    if len(keys) == 1:
        line = ""
        line_number = int(keys)
    else:
        line = keys[0].strip()
        line_number = int(keys[1])
    count += 1
    if count == 1:
        resevoir = line
        line_total = line_number
    else:
        line_total += line_number
        if random.uniform(0, 1) < line_number/float(line_total):
            resevoir = line
print(resevoir)
