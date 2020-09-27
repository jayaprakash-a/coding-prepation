#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *
class DisjointSet:
    def __init__(self):        
        self.parent = {}
        self.rank = {}
        self.count = Counter()
        self.maxValue = 0
    def find_parent(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
            self.count[x] = 1
        if self.parent[x] == x:
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find_parent(x)
        yset = self.find_parent(y)
        
        if xset == yset:
            return self.maxValue
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
            self.count[xset] += self.count[yset]            
            self.count[yset] = 0
        elif self.rank[yset] > self.rank[xset]:
            self.count[yset] += self.count[xset]            
            self.count[xset] = 0
            self.parent[xset] = yset
        else:
            self.parent[yset] = xset
            self.count[xset] += self.count[yset]            
            self.count[yset] = 0
            self.rank[xset] += 1
        self.maxValue = max(self.maxValue, self.count[yset], self.count[xset])
        return self.maxValue
def maxCircle(queries):
    obj = DisjointSet()
    # parent = {}
    # count = Counter()
    answer = []
    for [x, y] in queries: 
        
        answer.append(obj.union(x, y))
        # print(obj.count, obj.parent)
    return answer
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
