#!/usr/bin/python

import sys
import math

from bitarray import bitarray

error = 0.01
a = bitarray()

def bloom_filter(stream, n):
    array_size = int(math.ceil(-int(n)*math.log(error)/float(pow(math.log(2),2))))
    hash_num = int(round(array_size*math.log(2)/float(n)))
    res = []
    a = bitarray(array_size)
    a.setall(False)

    for i, line in enumerate(stream):
        if line=="":
            line = ""
        else:
            line = line.strip()
        if len(res) < int(n):
            hash_list = []
            for j in range(hash_num):
                hash_value = hash(str(j)+line)%array_size
                hash_list.append(hash_value)
            if i == 0:
                for key in hash_list:
                    a[key] = True
                res.append(line)
            else:
                count = 0
                for key in hash_list:
                    if a[key] == False:
                        a[key] = True
                        count += 1
                if count > 0:
                    res.append(line)
        else:
            break
    return res

result = bloom_filter(sys.stdin, sys.argv[1])
for line in result:
    print(line)
