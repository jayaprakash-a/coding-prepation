#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    opened, closed = '{[(', '}])'
    brackets = []
    for i in s:
        if i in opened:
            brackets.append(i)
        else:
            if len(brackets) == 0:
                return 'NO'
            ch = brackets.pop()
            if opened.index(ch) != closed.index(i):
                return 'NO'
    if len(brackets) == 0:
        return "YES"
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
