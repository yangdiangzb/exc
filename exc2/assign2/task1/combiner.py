#!/usr/bin/python

import sys

prev_word = ""
dic = {}
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    word = words[0]
    filename = words[1]
    count = int(words[2])
    if word != prev_word:
        if prev_word:
            for k,v in dic.items():
                print("{0}\t{1}\t{2}".format(prev_word,k,v))
            prev_word = ""
            dic = {}
        prev_word = word
        dic[filename] = count
    else:
        if filename in dic.keys():
            dic[filename] += count
        else:
            dic[filename] = count
if prev_word:
    for k,v in dic.items():
        print("{0}\t{1}\t{2}".format(prev_word,k,v))
    prev_word = ""
    dic = {}
