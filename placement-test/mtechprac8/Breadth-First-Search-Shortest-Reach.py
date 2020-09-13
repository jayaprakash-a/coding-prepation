#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *

# Complete the bfs function below.
def bfs(n, m, edges, s):
    edgeDict = defaultdict(list)
    # print(edges)
    for [x, y] in edges:
        edgeDict[x].append(y)
        edgeDict[y].append(x)
    dist = [-1 for _ in range(n)]
    edgeList = deque()
    dist[s-1] = 0
    for node in edgeDict[s]:
        if dist[node-1] == -1:
            dist[node-1] = 6
        edgeList.append(node)
    
    while edgeList:
        node = edgeList.pop()
        for adj in edgeDict[node]:
            if dist[adj-1] == -1:
                dist[adj-1] = dist[node-1] + 6
                edgeList.append(adj)
            elif dist[adj-1] > dist[node-1] + 6:
                dist[adj-1] = dist[node-1] + 6
                edgeList.append(adj)
    dist.pop(s-1)
    
    return dist
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
