#!/usr/bin/python

import sys

max_len_line = 0
max_len_token = 0

for line in sys.stdin:
    token1, token2 = line.strip().split()
    token1 = int(token1)
    token2 = int(token2)
    if token1 > max_len_token:
        max_len_token = token1
    if token2 > max_len_line:
        max_len_line = token2

print "{0} {1}".format(max_len_token, max_len_line)
