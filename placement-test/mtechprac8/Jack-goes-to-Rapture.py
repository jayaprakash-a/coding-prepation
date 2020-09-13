#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *
#
# Complete the 'getCost' function below.
#
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def getCost(g_nodes, g_from, g_to, g_weight):
    # Print your answer within the function and return nothing
    queue = deque([1])
    cost = [-1 for _ in range(g_nodes+1)]
    cost[1] = 0
    edgeWeights = defaultdict(list)
    for i in range(len(g_from)):
        edgeWeights[g_from[i]].append((g_to[i], g_weight[i]))
        edgeWeights[g_to[i]].append((g_from[i], g_weight[i]))
    queueSet = set([1])
    while queue:
        entry = queue.popleft()
        queueSet.remove(entry)
        if entry not in edgeWeights:
            continue
        for (adj, weight) in edgeWeights[entry]:            
            if cost[adj] != -1:
                if cost[adj] > cost[entry]:
                    if weight > cost[entry]:
                        newCost = weight
                    else:
                        newCost = cost[entry]
                    if cost[adj] > newCost:
                        if adj not in queueSet:
                            queue.append(adj)
                            queueSet.add(adj)
                        cost[adj] = newCost
            else:
                if adj not in queueSet:
                    queue.append(adj)
                    queueSet.add(adj)
                if weight > cost[entry]:
                    cost[adj] = weight
                else:
                    cost[adj] = cost[entry]
    if cost[g_nodes] != -1:
        print(cost[g_nodes])
    else:
        print('NO PATH EXISTS')
    
    
if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
