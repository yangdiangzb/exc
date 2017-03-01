#!/usr/bin/python

import sys

for line in sys.stdin:
    seq,value = line.strip().split(" ",1)
    if seq == "student":
        sid,sname = value.strip().split(" ",1)
        sname = sname.strip()
        print"{0}\t{1}\t{2}".format(sid,seq,sname)
    if seq == "mark":
        sid, cid = value.strip().split(" ",1)
        cid,score = cid.strip().split(" ",1)
        score = score.strip()
        print"{0}\t{1}\t({2},{3})".format(sid,seq,cid,score)
