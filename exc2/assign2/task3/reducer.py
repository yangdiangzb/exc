#!/usr/bin/python
import sys
from heapq import heappush, heappop
prev_id = ""

#heapq
h = []
for line in sys.stdin:
    uid,qids = line.strip().split("\t")
    if uid != prev_id:
        if prev_id:
            #keep heapq with size 1
            if h==[]:
                entry = [len(qid),prev_id,qid]
                heappush(h,entry)
            else:
                if len(qid) > int(h[0][0]):
                    heappop(h)
                    entry = [len(qid),prev_id,qid]
                    heappush(h,entry)
            prev_id=""
            qid = []
        prev_id = uid.strip()
        qid = qids.strip().split()
    else:
        qids = qids.strip().split()
        for key in qids:
            if key not in qid:
                qid.append(key.strip())
if prev_id:
    #keep heapq with size 1
    if h==[]:
        entry = [len(qid),prev_id,qid]
        heappush(h,entry)
    else:
        if len(qid) > int(h[0][0]):
            heappop()
            entry = [len(qid),prev_id,qid]
            heappush(h,entry)
    prev_id=""
    qid = []

print("{0} ->".format(h[0][1])),
i = 0
for key in h[0][2]:
    i += 1
    if i==1:
        print("{0}".format(key)),
    else:
        print(", {0}".format(key)),
print
