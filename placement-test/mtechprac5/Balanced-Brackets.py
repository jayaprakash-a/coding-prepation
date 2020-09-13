#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    opened, closed = ['(', '{', '['], [')', '}', ']']
    stack = []
    for ch in s:
        if ch in opened:
            stack.append(ch)
        else:
            if len(stack) == 0:
                return 'NO'
            last = stack.pop()
            if opened.index(last) == closed.index(ch):
                continue
            else:
                return 'NO'
    if len(stack) == 0:
        return 'YES'
    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
