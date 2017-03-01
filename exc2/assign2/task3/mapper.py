#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = line.strip()
    pattern1 = re.compile(r"ParentId\=\"(\d+)\"")
    pattern2 = re.compile(r"OwnerUserId\=\"(\d+)\"")
    pattern3 = re.compile(r"PostTypeId\=\"(\d+)\"")
    pid = pattern3.findall(line)

    if int(pid[0])==2:
        qid = pattern1.findall(line)
        uid = pattern2.findall(line)
        print("{0}\t{1}".format(int(uid[0]),int(qid[0])))
