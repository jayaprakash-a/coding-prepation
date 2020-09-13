#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    pivot = arr[0]
    count = 0
    left, right = [], []
    for i in range(len(arr)):
        if arr[i] < pivot:
            count += 1
            left.append(arr[i])
        else:
            right.append(arr[i])
    arr[0], arr[count] = arr[count], arr[0]
    for i in range(len(left)):
        arr[i] = left[i]
    for i in range(count, len(arr)):
        arr[i] = right[i-count]
    return arr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
