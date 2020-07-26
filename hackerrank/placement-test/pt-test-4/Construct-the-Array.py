#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countArray function below.
def countArray(n, k, x):
    modVal = 10**9 + 7
    dp = [1, 0]
    print(dp)
    while(n - 2):
        n -= 1
        temp = dp[0]
        dp[0] = (dp[1] + (k-2)*dp[0])%(modVal)
        dp[1] = ((k-1)*temp)%(modVal)
    if x != 1:
        return dp[0]
    else:
        return dp[1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
