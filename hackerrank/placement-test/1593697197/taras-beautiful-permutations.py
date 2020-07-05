#!/bin/python3

import os
import sys
import math

#
# Complete the beautifulPermutations function below.
#
def beautifulPermutations(arr):
    n = len(arr)
    k = n - len(set(arr))
    modVal = 10**9 + 7
    if k == 0:
        return math.factorial(n) % modVal
    vals = [0 for _ in range(k)]
    
    vals[0] = (k*math.factorial(n-1))//(1<<(k-1)) 
    for i in range(1, k):
        vals[i] = -1 * ((vals[i-1]*(k-i)*2)//((i+1)*(n-i)))
    value = sum(vals) % modVal
    answer = (math.factorial(n)//(1<<k)% modVal) - value
    return answer % modVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = beautifulPermutations(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
