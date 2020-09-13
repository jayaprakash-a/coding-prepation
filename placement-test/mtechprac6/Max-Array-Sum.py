#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    if len(arr) <= 2:
        return max(max(arr), 0)
    dp1 = [0 for _ in range(len(arr))]
    dp1[0] = arr[0]
    dp1[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        dp1[i] = max(dp1[i], dp1[i-2], dp1[i-2]+arr[i], dp1[i-1])
    return dp1[-1]
        
if __name__ == '__main__':
    fptr = open('ans.txt', 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
