#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n, m):
    N = (n+m)
    M = min(n, m)
    answer = 1
    fact = 1
    for i in range(1, M+1):
        fact *= i
        answer *= (N-i+1)
    return (answer//fact) %(10**9+7)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
