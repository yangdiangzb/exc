#!/usr/bin/python

import sys

prev_id = ""
dic={}

for line in sys.stdin:
    uid,qid = line.strip().split()
    count = 1
    if uid != prev_id:
        if prev_id:
            print ("{0}\t".format(prev_id)),
            for k in dic.keys():
                print(k),
            print
            dic={}
            prev_id=""
        prev_id = uid
        dic[qid] = count
    else:
        if qid in dic.keys():
            dic[qid] += count
        else:
            dic[qid] = count
if prev_id:
    print ("{0}\t".format(prev_id)),
    for k in dic.keys():
        print(k),
    print
    dic={}
    prev_id=""
