#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    # n = n
    while len(n) != 1:
        sumVal = 0
        for ch in n:
            sumVal += int(ch)
        n = str(sumVal)
    n = str(int(n)*k)
    while len(n) != 1:
        sumVal = 0
        for ch in n:
            sumVal += int(ch)
        n = str(sumVal)
    return n
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
