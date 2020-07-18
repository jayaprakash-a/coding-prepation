#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr = sorted(arr)
    minDiff = min([arr[i]-arr[i-1] for i in range(1, len(arr))])
    result = []
    for i in range(1, len(arr)):
        if arr[i]-arr[i-1] == minDiff:
            result.append(arr[i-1])
            result.append(arr[i])
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
