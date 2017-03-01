#!/usr/bin/python

import sys
from heapq import heappush, heappop

h = [] #heapq
prev_id = ""
aid_list = []

for line in sys.stdin:
    uid,aid = line.strip().split()
    if uid != prev_id:
        if prev_id:
            #keep heapq with size 1
            if h==[]:
                entry = [len(aid_list),prev_id,aid_list]
                heappush(h,entry)
            else:
                if len(aid_list) > int(h[0][0]):
                    heappop(h)
                    entry = [len(aid_list),prev_id,aid_list]
                    heappush(h,entry)
            prev_id = ""
            aid_list = []
        prev_id = uid
        aid_list.append(int(aid))
    else:
        if int(aid) not in aid_list:
            aid_list.append(int(aid))

if prev_id:
    if h==[]:
        entry = [len(aid_list),prev_id,aid_list]
        heappush(h,entry)
    else:
        if len(aid_list) > int(h[0][0]):
            heappop(h)
            entry = [len(aid_list),prev_id,aid_list]
            heappush(h,entry)
    prev_id = ""
    aid_list = []


print("{0} -> {1}".format(h[0][1],h[0][0])),
for key in h[0][2]:
        print(", {0}".format(key)),
print
