#!/bin/python3

import os
import sys

#
# Complete the arraySplitting function below.
#
def arraySplitting(arr):
    if arr == [0 for _ in range(len(arr))]:
        return len(arr)-1
    # print(arr)
    if len(arr) <= 1:
        return 0
    sumVal = sum(arr)
    if sumVal % 2 == 1:
        return 0
    preSum = 0
    for i, num in enumerate(arr):
        preSum += num
        if preSum == sumVal // 2:
            return 1 + max(arraySplitting(arr[:(i+1)]), arraySplitting(arr[(i+1):]))
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = arraySplitting(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
