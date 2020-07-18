import math
import os
import random
import re
import sys
import bisect
# Complete the maximumSum function below.
def maximumSum(a, m):
    for i in range(len(a)):
        a[i] %= m
    preSum, maxVal = 0, 0
    numSet = []
    for i in range(len(a)):
        preSum = (preSum+a[i])%m
        maxVal = max(maxVal, preSum)
        if maxVal == m-1:
            return maxVal
        numSet.append(preSum) 
        
    pq = [numSet[0]]
    for i in range(1, len(a)):
        left = bisect.bisect_right(pq, numSet[i])
        if left != len(pq):
            maxVal = max(maxVal, (numSet[i] - pq[left]) % m)
            if maxVal == m-1:
                return maxVal
        index = bisect.bisect_left(pq, numSet[i]) 
        if index == len(pq) or pq[index] != numSet[i]: 
            bisect.insort(pq, numSet[i])
    return maxVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
