#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    impLuck = []
    total = 0
    for luck, imp in contests:
        # print(luck, imp)
        if imp == 1:
            impLuck.append(luck)
        else:
            total += luck
    impLuck = sorted(impLuck)
    if k <= len(impLuck):
        for i in range(len(impLuck)-k):
            total -= impLuck[i]
        for i in range(len(impLuck)-k, len(impLuck)):
            total += impLuck[i]
    else:
        for i in range(len(impLuck)):
            total += impLuck[i]

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
