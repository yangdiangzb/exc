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
            print("{0} : {1} :".format(prev_word,len(dic))),
            print("{"),
            i=0
            for k,v in sorted(dic.items()):
                i += 1
                if i == 1:
                    print("({0}, {1})".format(k,v)),
                else:
                    print(", ({0}, {1})".format(k,v)),
            print("}")

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
    print("{0} : {1} :".format(prev_word,len(dic))),
    print("{"),
    i=0
    for k,v in sorted(dic.items()):
        i += 1
        if i == 1:
            print("({0}, {1})".format(k,v)),
        else:
            print(", ({0}, {1})".format(k,v)),
    print("}")
prev_word = ""
dic = {}
