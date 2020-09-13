#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *
import heapq

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


def kruskals(g_nodes, g_from, g_to, g_weight):
    weights = []
    
    obj = DisjointSet(g_nodes) 
    edgeWeights = defaultdict(list)
    for i in range(len(g_from)):
        edgeWeights[g_weight[i]].append((g_from[i], g_to[i]))
    for weight in edgeWeights:
        edgeWeights[weight] = sorted(edgeWeights[weight], key = lambda x:(x[0]+x[1]), reverse=True)
    heapq.heapify(g_weight)
    count = 0
    answer = 0
    while count < g_nodes - 1:
        weight = heapq.heappop(g_weight)
        edge = edgeWeights[weight].pop()
        if obj.find_parent(edge[0]-1) != obj.find_parent(edge[1]-1):
            answer += weight
            count += 1
            obj.union(edge[0]-1, edge[1]-1)
    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)
    # print(res)
    # Write your code here.
    fptr.write(str(res) + '\n')
    fptr.close()
