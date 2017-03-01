#!/usr/bin/python
import sys

key = ""
count = 0

for line in sys.stdin:
    key2 = line.strip()
    value = 1
    if key2 != key:
        if key:
            if count == 1:
                print(key)
        key,count = key2, value
    else:
        count += value
if key:
    if count == 1:
        print(key)
