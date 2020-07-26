#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
from collections import *
# Complete the shortestReach function below.
def shortestReach(n, edges, start):
    maxLen = sum([edges[i][2] for i in range(len(edges))])
    edgeWeight = {}
    edgeList = defaultdict(list)
    for [s,d,w] in edges:
        if s-1 not in edgeWeight:
            edgeWeight[s-1] = {}
        if d-1 not in edgeWeight:
            edgeWeight[d-1] = {}
        if d-1 in edgeWeight[s-1]:
            edgeWeight[s-1][d-1] = max(w, edgeWeight[s-1][d-1])
        else:
            edgeWeight[s-1][d-1] = w
        if s-1 in edgeWeight[d-1]:
            edgeWeight[d-1][s-1] = max(w, edgeWeight[d-1][s-1])
        else:
            edgeWeight[d-1][s-1] = w
    for s in edgeWeight:
        for d in edgeWeight[s]:
            edgeList[s-1].append([d-1, edgeWeight[s][w]])
    # print(edgeList)
    edgeDist = [[i, maxLen+1] for i in range(n)]
    edgeDist[start-1][1] = 0
    distance = [[0, start-1]]
    heapq.heapify(distance)
    # print(edgeDist)
    while len(distance) != 0:
        node = heapq.heappop(distance)
        # print('Node', node)
        for [dest, weight] in edgeList[node[1]]:
            if edgeDist[dest][1] > edgeDist[node[1]][1] + weight:
                edgeDist[dest][1] = edgeDist[node[1]][1] + weight
                isPresent = False
                for i in range(len(distance)):
                    if distance[i][1] == dest:
                        distance[i][0] = edgeDist[dest][1]
                        heapq.heapify(distance)
                        isPresent = True
                        break
                if not isPresent:
                    heapq.heappush(distance, [edgeDist[dest][1], dest])
                # print(edgeDist)
    answer = [edgeDist[i][1]  for i in range(n) if i != start-1]
    answer = [entry if entry != maxLen+1 else -1 for entry in answer]
    return answer    maxLen = sum([edges[i][2] for i in range(len(edges))])
    edgeList = defaultdict(list)
    for [s,d,w] in edges:
        edgeList[s-1].append([d-1, w])
        edgeList[d-1].append([s-1, w])
    # print(edgeList)
    edgeDist = [[i, maxLen+1] for i in range(n)]
    edgeDist[start-1][1] = 0
    distance = [[0, start-1]]
    heapq.heapify(distance)
    # print(edgeDist)
    while len(distance) != 0:
        node = heapq.heappop(distance)
        # print('Node', node)
        for [dest, weight] in edgeList[node[1]]:
            if edgeDist[dest][1] > edgeDist[node[1]][1] + weight:
                edgeDist[dest][1] = edgeDist[node[1]][1] + weight
                isPresent = False
                for i in range(len(distance)):
                    if distance[i][1] == dest:
                        distance[i][0] = edgeDist[dest][1]
                        heapq.heapify(distance)
                        isPresent = True
                        break
                if not isPresent:
                    heapq.heappush(distance, [edgeDist[dest][1], dest])
                # print(edgeDist)
    answer = [edgeDist[i][1]  for i in range(n) if i != start-1]
    answer = [entry if entry != maxLen+1 else -1 for entry in answer]
    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
