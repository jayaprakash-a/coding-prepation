#!/bin/python3

import math
import os
import random
import re
import sys
import collections
# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    value = collections.Counter(arr)
    count = [(k, v) for k, v in value.items()] 
    return min(count, key=lambda x:(-x[1], x[0]))[0]
    # return answer[0]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
