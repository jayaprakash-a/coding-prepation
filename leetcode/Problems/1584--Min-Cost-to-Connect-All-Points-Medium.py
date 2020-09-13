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



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        obj = DisjointSet(len(points)) 
        edgeWeights = defaultdict(list)
        weights = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                weight = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                weights.append(weight)
                edgeWeights[weight].append((i, j))
        for weight in edgeWeights:
            edgeWeights[weight] = sorted(edgeWeights[weight], key = lambda x:(x[0]+x[1]), reverse=True)
        heapq.heapify(weights)
        count = 0
        answer = 0
        while count < len(points) - 1:
            weight = heapq.heappop(weights)
            edge = edgeWeights[weight].pop()
            if obj.find_parent(edge[0]) != obj.find_parent(edge[1]):
                answer += weight
                count += 1
                obj.union(edge[0], edge[1])
        return answer
        
        
        