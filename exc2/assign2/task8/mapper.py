#!/usr/bin/python

import sys
import math

s = 0.01
error = 0.001
window_size = math.ceil(1/error)


def lossy_count(stream):
    j = 0
    line_number = 0
    result = []
    freq={}
    bcur={}
    for i,line in enumerate(stream):
        line_number += 1
        b_current = math.ceil(line_number/window_size)
        if line in freq.keys():
            freq[line] += 1
            j += 1
        else:
            freq[line] = 1
            j += 1
            bcur[line] = b_current - 1
        #after counting one window
        if j == window_size:
            for k,v in freq.items():
                if freq[k] + bcur[k] <= b_current:
                    del freq[k]
                    del bcur[k]
            j = 0
    for k,v in freq.items():
        #last window which is less window_size
        if freq[k] >= math.ceil((s-error)*line_number):
            result.append(k)
    return result

result = lossy_count(sys.stdin)
for line in result:
    sys.stdout.write(line)
