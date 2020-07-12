#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    dp = [[0 for _ in range(len(c))] for _ in range(n+1)]
    for i in range(len(c)):
        dp[0][i] = 1
    for i in range(1, n+1):
        for j in range(len(c)):
            coin = c[j]
            if coin <= i:
                dp[i][j] += dp[i-coin][j]
            dp[i][j] += dp[i][j-1]
    print(dp)
    return dp[n][len(c)-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
