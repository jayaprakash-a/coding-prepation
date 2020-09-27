#!/bin/python3

import os
import sys
from collections import *
import heapq



def rustMurdered(n, edgeWeights, s):
    print('---------------')
    print(edgeWeights)
    notVisited = set(list(range(n)))
    cost = [sys.maxsize for _ in range(n)]
    queue = deque([s])
    notVisited.remove(s)
    cost[s] = 0
    while queue:
        entry = queue.popleft()
        neighbours = []
        for unvisited in notVisited:
            if unvisited not in edgeWeights[entry]:
                neighbours.append(unvisited)
        print(entry, neighbours)
        for adj in neighbours:            
            if cost[adj] > cost[entry]+1:
                queue.append(adj)                
                cost[adj] = cost[entry]+1
            notVisited.remove(adj)
    cost.pop(s)    
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(sys.stdin.readline().rstrip())
    for t_itr in range(t):
        nm = sys.stdin.readline().rstrip().split()
        n = int(nm[0])
        m = int(nm[1])
        roads = defaultdict(set)
        for _ in range(m):
            edge = tuple(map(int, sys.stdin.readline().rstrip().split()))
            roads[edge[0]-1].add(edge[1]-1)
            roads[edge[1]-1].add(edge[0]-1)
        s = int(input())
        result = rustMurdered(n, roads, s-1)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
