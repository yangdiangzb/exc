#!/usr/bin/python

import sys
dic={}
for line in sys.stdin:
    count, qid = line.strip().split()
    dic[int(count)] = int(qid)
for k,v in sorted(dic.items(),reverse=True)[:10]:
    print("{0} {1}".format(k,v))
