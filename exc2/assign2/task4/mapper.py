#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = line.strip()
    pattern1 = re.compile(r"PostTypeId\=\"(\d+)\"")
    pattern2 = re.compile(r"AcceptedAnswerId\=\"(\d+)\"")
    pattern3 = re.compile(r"OwnerUserId\=\"(\d+)\"")
    pattern4 = re.compile(r"Id\=\"(\d+)\"")
    pid = pattern1.findall(line)

    if int(pid[0]) == 1:
        acceptId = pattern2.findall(line)
        if acceptId:
            print("{0}\tAcceptedAnswerId".format(int(acceptId[0])))
    elif int(pid[0]) == 2:
        uid = pattern3.findall(line)
        aid = pattern4.findall(line)
        print("{0}\t{1}".format(int(aid[0]),int(uid[0])))
