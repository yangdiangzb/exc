#!/usr/bin/python

import sys
import re
from heapq import heappush, heappop

i = 0
#heapq
h = []
for line in sys.stdin:
    line = line.strip()
    pattern1 = re.compile(r"PostTypeId\=\"(\d+)\"")
    pattern2 = re.compile(r"ViewCount\=\"(\d+)\"")
    pattern3 = re.compile(r"Id\=\"(\d+)\"")
    pid = pattern1.findall(line)

    if int(pid[0]) == 1:
        i+=1
        viewcount = pattern2.findall(line)
        qid = pattern3.findall(line)
        viewcount = int(viewcount[0])
        qid = int(qid[0])
        #keep heapq has 10 records
        if i <=10:
            heappush(h,(viewcount,qid))
        else:
            if viewcount > int(h[0][0]):
                heappop(h)
                heappush(h,(viewcount,qid))
for k in h:
    print("{0} {1}".format(k[0],k[1]))
