#!/usr/bin/python

import sys
import math
prev_id = ""

for line in sys.stdin:
    sid, con, info= line.strip().split("\t")

    if sid != prev_id:
        if prev_id:
            print "{0} --> {1}".format(sname,slist)
        sname = ""
        slist = ""
        if con == "student":
            prev_id = sid
            sname = info
        elif con == "mark":
            prev_id = sid
            slist = info
    else:
        if con == "student":
            sname = info
        elif con == "mark":
            if slist == "":
                slist += info
            else:
                slist += " " + info
if prev_id:
    print "{0} --> {1}".format(sname,slist)
