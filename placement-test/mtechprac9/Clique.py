#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'clique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def clique(n, m):
    # Write your code here
    def getNum(r):
        if r < 1:
            return 1
        # return (n*n - (n%r)*math.ceil(n/r)*math.ceil(n/r) - (r - (n%r))*math.floor(n/r)*math.floor(n/r))/2
        return ((n**2 - (n%r)*(math.ceil(n/r)**2) - (r - (n%r))*(math.floor(n/r)**2) ))//2
    low, high = 1, n
    answer = -1
    # for i in range(low+1, high+2):
    #     print(i, getNum(i))
    #     if getNum(i) >= m:
    #         return i
    while low <= high:       
        mid = (low+high)//2        
        num = getNum(mid)
        if m <= num:
            answer = mid
            high = mid-1
        else:
            low = mid+1
    return answer
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = clique(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
