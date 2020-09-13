import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    vals = set()
    count = 0
    for num in arr:
        if k+num in vals:
            count += 1
        if num-k in vals:
            count += 1
        vals.add(num)
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
