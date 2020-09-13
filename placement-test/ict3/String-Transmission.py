#!/bin/python3

import os
import sys

#
# Complete the stringTransmission function below.
#
def stringTransmission(k, s):
    print('-------------')
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    def check(s):
        if len(s) == 1:
            return True
        
        for i in range(1, len(s)//2+1):
            new = s[:i]
            if new*(len(s)//len(new)) == s:
                return True
        return False
    for i in range(1, n+1):
        if not check(s[:i]):
            dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] += dp[i-1][j]
            print(check(s[:i-1] + str(1-int(s[i-1]))), s[:i])
            if not check(s[:i-1] + str(1-int(s[i-1]))):
                dp[i][j] += dp[i-1][j-1]
    print(dp)
    return sum(dp[-1][i] for i in range(k+1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        s = input()

        result = stringTransmission(k, s)

        fptr.write(str(result) + '\n')

    fptr.close()
