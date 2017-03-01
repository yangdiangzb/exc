#!/usr/bin/python

import sys
import random

def resevoir_sample(stream, n):
    resevoir = []

    for i, line in enumerate(stream):
        if i < n:
            resevoir.append(line)
        else:
            rand = random.randint(0, n)
            if rand < n:
                resevoir[rand] = line
    return resevoir


sample = resevoir_sample(sys.stdin, 100)
for line in sample:
    sys.stdout.write(line)
