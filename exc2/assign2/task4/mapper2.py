#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    ids = line.strip().split()
    print("{0}\t{1}".format(int(ids[1]),int(ids[0])))
