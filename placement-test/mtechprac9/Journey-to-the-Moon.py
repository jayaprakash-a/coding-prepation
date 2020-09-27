#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    def find_parent(self, x):
        if self.parent[x] == x:
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xset = self.find_parent(x)
        yset = self.find_parent(y)
        if xset == yset:
            return
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        elif self.rank[yset] > self.rank[xset]:
            self.parent[xset] = yset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1

# Complete the journeyToMoon function below.
def journeyToMoon(n, astronaut):
    obj = DisjointSet(n)
    for [x, y] in astronaut:
        obj.union(x, y)
    country = Counter()
    unknown = 0
    for i in range(len(obj.parent)):
        if obj.find_parent(i) != i:
            country[obj.parent[i]] += 1
    for i in range(len(obj.parent)):
        if obj.parent[i] == i and obj.parent[i] not in country:
            unknown += 1
        elif obj.parent[i] == i and obj.parent[i] in country:
            country[obj.parent[i]] += 1
    entries = list(country.keys())
    answer = 0
    for i in range(len(entries)):
        for j in range(i+1, len(entries)):
            answer += country[entries[i]]*country[entries[j]]
    answer += ((n-unknown)*unknown)
    answer += (unknown*(unknown-1)//2)
    # print(obj.parent, country, unknown)
    return answer
                   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    np = input().split()

    n = int(np[0])

    p = int(np[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, sys.stdin.readline().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
