#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *
import heapq
# Complete the shortestReach function below.
def shortestReach(n, minEdge, source):

    cost = [sys.maxsize for _ in range(n+1)]
    pq = [(0, source)]
    cost[source] = 0
    queueEntry = set([source])
    while len(pq) > 0:
        _, minInd = heapq.heappop(pq)
        queueEntry.remove(minInd)
        for adj in minEdge[minInd]:
            weight = minEdge[minInd][adj]
            if cost[minInd] + weight < cost[adj]:
                cost[adj] = cost[minInd] + weight
                if adj not in queueEntry:
                    heapq.heappush(pq, (cost[adj], adj))
                    queueEntry.add(adj)
        
    if len(cost) > source:
        cost.pop(source)
    if len(cost) > 0:
        cost.pop(0)
    for i in range(len(cost)):
        if cost[i] == sys.maxsize:
            cost[i] = -1
    return cost
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])
        minEdge = defaultdict(dict)
        # edges = []

        for _ in range(m):
            [s, d, w] = list(map(int, sys.stdin.readline().rstrip().split()))
            if d in minEdge[s]:
                minEdge[s][d] = min(w, minEdge[s][d])
            else:
                minEdge[s][d] = w
            if s in minEdge[d]:
                minEdge[d][s] = min(w, minEdge[d][s])
            else:
                minEdge[d][s] = w
        s = int(input())

        result = shortestReach(n, minEdge, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
