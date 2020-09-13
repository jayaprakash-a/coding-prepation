import math
import os
import random
import re
import sys
import bisect
#
# Complete the 'search' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER x
#  3. INTEGER_ARRAY arr
#

def search(n, x, arr):
    index = bisect.bisect_left(arr, x)
    if  0 <= index < len(arr):
        if arr[index] == x:
            return 'YES'
    return 'NO'
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    q = int(input().strip())

    for q_itr in range(q):
        x = int(input().strip())

        result = search(n, x, arr)

        fptr.write(result + '\n')

    fptr.close()
