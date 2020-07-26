#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    def median(heap1, heap2, d):
        if d % 2 == 1:
            return heap2[0][0] * 1.0  
        else:
            return (heap2[0][0]-heap1[0][0]) / 2
    def transfer(heap1, heap2):
        (num, index) = heapq.heappop(heap1)
        heapq.heappush(heap2, (-num, index))
    small, large = [], []
    for i in range(d):
        heapq.heappush(small, (-1*expenditure[i], i))
    for _ in range(d-(d>>1)): 
        transfer(small, large)
    # print(small, large)
    # print(small[0][0], large[0][0])
    answer = 0
    for i in range(d, len(expenditure)):
        val = median(small, large, d)
        if expenditure[i] >= 2*val:
            answer += 1
        if expenditure[i] >= large[0][0]:
            heapq.heappush(large, (expenditure[i], i))
            if expenditure[i-d] <= large[0][0]:
                transfer(large, small)
        else:
            heapq.heappush(small, (-1*expenditure[i], i))
            if expenditure[i-d] >= large[0][0]:
                transfer(small, large)   
        while small and small[0][1] <= i-d: 
            heapq.heappop(small)
        while large and large[0][1] <= i-d: 
            heapq.heappop(large)
    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
