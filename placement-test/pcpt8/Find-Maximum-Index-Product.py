#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(arr):
    
    def getLeft(arr):
        stack = []
        result = [0 for _ in range(len(arr))]
        for i in range(len(arr)):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            if len(stack) == 0:
                result[i] = 0
            else:
                result[i] = stack[-1]+1
            stack.append(i)
        return result
    def getRight(arr):
        stack = []
        result = [0 for _ in range(len(arr))]
        for i in range(len(arr)-1, -1, -1):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            if len(stack) == 0:
                result[i] = 0
            else:
                result[i] = stack[-1]+1
            stack.append(i)
        return result
    left, right = getLeft(arr), getRight(arr)
    print(left, right)
    maxVal = 0
    for i in range(len(left)):
        maxVal = max(maxVal, (left[i])*(right[i]))
    return maxVal
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
