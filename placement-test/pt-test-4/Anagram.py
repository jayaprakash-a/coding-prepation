#!/bin/python3

import math
import os
import random
import re
import sys
import collections
# Complete the anagram function below.
def anagram(s):
    if len(s)%2 == 1:
        return -1
    c1 = collections.Counter(s[:(len(s)//2)])
    c2 = collections.Counter(s[(len(s)//2):])
    d = c1 - (c1&c2)
    return sum(d.values())
    # print(c1, c2, c1&c2, c1 - (c1&c2))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
