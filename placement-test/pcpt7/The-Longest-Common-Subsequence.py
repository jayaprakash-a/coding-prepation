#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the longestCommonSubsequence function below.
def longestCommonSubsequence(a, b):
    dp = [[[0, ''] for _ in range(len(b)+1)]  for _ in range(len(a)+1)]
    
    for i in range(len(a)):
        for j in range(len(b)):
            if i == 0 or j == 0:
                dp[i][j][0] = 0
            if a[i] == b[j]:
                dp[i+1][j+1][0] = dp[i][j][0] + 1
                dp[i+1][j+1][1] = dp[i][j][1] + str(a[i]) + ' '
            else:
                if dp[i][j+1][0] >= dp[i+1][j][0]:
                    dp[i+1][j+1][0] = dp[i][j+1][0]
                    dp[i+1][j+1][1] = dp[i][j+1][1]
                else:
                    dp[i+1][j+1][0] = dp[i+1][j][0]
                    dp[i+1][j+1][1] = dp[i+1][j][1]
    print(dp[-1][-1][1])
    answer = map(int, dp[-1][-1][1].split())
    return answer
        
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
