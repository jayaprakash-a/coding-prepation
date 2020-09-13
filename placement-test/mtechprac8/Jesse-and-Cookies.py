#!/bin/python3

import os
import sys
import heapq
#
# Complete the cookies function below.
#
def cookies(k, A):
    heapq.heapify(A)
    count = 0
    while len(A) > 0:
        e1, e2 = heapq.heappop(A), 0
        if e1 >= k:
            break
        if len(A) > 0:
            e2 = heapq.heappop(A)
            count += 1
        else:
            return -1
        e3 = e1 + 2*e2
        heapq.heappush(A, e3)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
