#!/usr/bin/python

import sys

prev_id = ""
ans_list = []

for line in sys.stdin:
    aid,uid = line.strip().split()
    if aid != prev_id:
        if prev_id:
            if "AcceptedAnswerId" in ans_list:
                if len(ans_list) !=1:
                    print(int(prev_id)),
                    for key in ans_list:
                        if key != "AcceptedAnswerId":
                            print(int(key)),
                    print
            prev_id = ""
            ans_list = []
        prev_id = aid
        ans_list.append(uid)
    else:
        ans_list.append(uid)
if prev_id:
    if "AcceptedAnswerId" in ans_list:
        if len(ans_list) !=1:
            print(int(prev_id)),
            for key in ans_list:
                if key != "AcceptedAnswerId":
                    print(int(key)),
            print
    prev_id = ""
    ans_list = []
