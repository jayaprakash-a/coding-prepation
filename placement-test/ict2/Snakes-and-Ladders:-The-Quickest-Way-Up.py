#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *

# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    q = deque([(1, 0)])
    l, s = {}, {}
    for [k, v] in ladders:
        l[k] = v
    for [k, v] in snakes:
        s[k] = v
    best = {1: 0}
    while q:
        entry = q.popleft()

        for i in range(entry[0]+1, min(101, entry[0]+7)):
            val = i
            if i in l:
                val = l[i]
            elif i in s:
                val = s[i]
            if val in best and best[val] > entry[1] + 1:
                q.append((val, entry[1] + 1))
                best[val] = entry[1] + 1
            elif val not in best:
                q.append((val, entry[1] + 1))
                best[val] = entry[1] + 1


    if 100 in best:
        return best[100]
    return -1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
