#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *

def isValid(a, b):
    # print('Check', a, b, len(a), len(b), len(b) != len(a)+1)
    if len(b) != len(a)+1:
        return False
    i, j = 0, 0
    while i < len(a):
        if j >= len(b):
            break
        if a[i] != b[j]:
            j += 1
        else:
            j += 1
            i += 1
    return i == len(a)

def solve(n, words):
    # print(len(words))
    words = list(set(words))
    # print(len(words))
    words = sorted(words, key=len)
    dp = [1 for _ in range(len(words))]
    prev = [-1  for _ in range(len(words))]
    adjWords = defaultdict(list)
    maxVal, maxInd = 1, 0
    for i in range(len(words)):
        for j in range(i):
            # print(words[j], words[i], isValid(words[j], words[i]))
            if isValid(words[j], words[i]) and dp[i] < dp[j]+1:
                dp[i] = dp[j] + 1
                prev[i] = j
                if dp[i] > maxVal:
                    maxVal = dp[i]
                    maxInd = i
                    
    print(dp[maxInd])
    answer = []
    while maxInd != -1:
        answer.append(words[maxInd])
        maxInd = prev[maxInd]
    print('\n'.join(answer[::-1]))
                

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input().strip()
        words.append(words_item)

    solve(n, words)
