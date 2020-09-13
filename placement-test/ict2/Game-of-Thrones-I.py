#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *
# Complete the gameOfThrones function below.
def gameOfThrones(s):
    sc = Counter(s)
    oc, ec = 0, 0
    for key in sc:
        if sc[key]%2 == 1:
            oc += 1
        else:
            ec += 1
    if oc == 0:
        return 'YES'
    elif oc == 1:
        return 'YES'
    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
