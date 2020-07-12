#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    used = [False for _ in range(n)]
    answer = [0 for _ in range(n)]
    for i in range(n):
        if i>=k and not used[i-k]:
            answer[i] = i+1-k
            used[i-k] = True
        elif i+k < n and not used[i+k]:
            answer[i] = i+1+k
            used[i+k] = True
        else:
            return [-1]
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
