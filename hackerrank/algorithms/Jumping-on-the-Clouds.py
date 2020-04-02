#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    count = 0
    while(i < len(c)):
        if (i+2) < len(c) and c[i+2] == 0:
            i += 2
        else:
            i += 1
        count += 1
        if i == len(c)-1:
            break
        
        # print(i, count)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
