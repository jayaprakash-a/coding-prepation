#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    answer, sumVal = 0, 0
    i, j, alen, blen = 0, 0, len(a), len(b)
    while i < alen and sumVal + a[i] <= x:
        sumVal += a[i]
        i += 1
    answer = i
    
    while j < blen and i >= 0:
        sumVal += b[j]
        j += 1
        while i >=0 and sumVal > x:
            i -= 1
            sumVal -= a[i]
            
        if sumVal <= x:
            answer = max(answer, i+j)
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
