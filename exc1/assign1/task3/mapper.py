#!/usr/bin/python

import sys


max_len_line = 0 #max length of line
max_len_token = 0 #max length of token

for line in sys.stdin:
    len_line = len(line.strip())
    if len_line > max_len_line:
        max_len_line = len_line
    tokens = line.split()

    for token in tokens:
        len_token = len(token)
        if len_token > max_len_token:
            max_len_token = len_token

print "{0} {1}".format(max_len_token, max_len_line)
