#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    stack = []
    maxArea = 0
    index = 0
    while index < len(h):
        if not stack or h[stack[-1]] <= h[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            if stack:
                newArea = h[top]*(index-stack[-1]-1)
            else:
                newArea = h[top]*(index)
            maxArea = max(maxArea, newArea)
    
    while stack:
        top = stack.pop()
        if stack:
            newArea = h[top]*(index-stack[-1]-1)
        else:
            newArea = h[top]*(index)
        maxArea = max(maxArea, newArea)
    
    return maxArea
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
