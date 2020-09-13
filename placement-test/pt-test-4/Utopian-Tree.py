#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(answer, n):
    return answer[n]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())
    answer = [1]
    for i in range(1, 61):
        if i%2 == 1:
            answer.append(2*answer[-1])
        else:
            answer.append(answer[-1] +1 )
        
    for t_itr in range(t):
        n = int(input())

        result = utopianTree(answer, n)

        fptr.write(str(result) + '\n')

    fptr.close()
