#!/usr/bin/python
import sys

for line in sys.stdin:
        name, scores =line.strip().split("-->")
        name = name.strip()
        scores = scores.strip().split()
        if scores != []:
                count = 0
                total = 0
                grades=[]
                for score in scores:
                        count += 1
                        course, grade = score.split(",")
                        grade= grade.strip().split(")")
                        grades.append(grade[0])
                        total += int(grade[0])
                if count > 3:
                        avg = total/float(count)
                        print("{0} {1}".format(name,avg))
