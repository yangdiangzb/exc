#!/usr/bin/python

import sys
token = []
for line in sys.stdin:
    tokens = line.strip().split()
    for i in range(0, len(tokens)-2):
        token = tokens[i] + " " + tokens[i+1] + " " + tokens[i+2]
        print("{0}\t{1}".format(token,1))
