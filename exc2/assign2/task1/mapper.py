#!/usr/bin/python

import sys
import os

filepath = os.environ["map_input_file"]
filename = os.path.split(filepath)[-1]
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print("{0}\t{1}\t1".format(word,filename))
