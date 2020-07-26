#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    newArr = []
    for i in range(len(arr)):
        newArr.append(tuple([i]+arr[i]))
    mapping = {}
    for i in range(len(newArr)//2):
        mapping[newArr[i]] = '-'
    newArr = sorted(newArr, key=lambda x: int(x[1]))
    answer = []
    for entry in newArr:
        if entry in mapping:
            answer.append('-')
        else:
            answer.append(entry[2])
    print(' '.join(answer))
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
