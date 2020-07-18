import math
import os
import random
import re
import sys
import collections
def solve(n, q, parents, a, d):
    depths = collections.Counter()
    depths[1] = 0
    depthXor = {}
    depthXor[0] = a[0]   
    
    children = collections.defaultdict(list)
    for i in range(len(parents)):
        print(i+2, parents[i])
        children[parents[i]] += [i+2]
    def bfs(node):
        nodes = collections.deque()
        for child in children[node]:
            depths[child] = depths[node]+1
            if depths[node]+1 not in depthXor:
                depthXor[depths[node]+1] = a[child-1]
            else:
                depthXor[depths[node]+1] ^= a[child-1]
        
            nodes.append(child)
        while nodes:
            node = nodes.popleft()
            for child in children[node]:
                depths[child] = depths[node]+1
                if depths[node]+1 not in depthXor:
                    depthXor[depths[node]+1] = a[child-1]
                else:
                    depthXor[depths[node]+1] ^= a[child-1]
                nodes.append(child)
    bfs(1)
    maxDepth = max(depths.values())
    for depth in range(1, maxDepth+1):
        depthXor[depth] ^= depthXor[depth-1]
    answer = []
    depthXor[-1] = 0
    for [d1, d2] in d:
        val = depthXor[d2] ^ depthXor[d1-1]
        answer.append(val)
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    parents = list(map(int, input().rstrip().split()))

    a = list(map(int, input().rstrip().split()))

    q = int(input().strip())

    d = []

    for _ in range(q):
        d.append(list(map(int, input().rstrip().split())))

    result = solve(n, q, parents, a, d)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
