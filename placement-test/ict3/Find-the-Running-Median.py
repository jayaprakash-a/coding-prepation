#!/bin/python3

import os
import sys
import heapq
#
# Complete the runningMedian function below.
#
def runningMedian(a):
    small, big = [], []
    values = []
    for num in a:
        if len(small) == 0:
            heapq.heappush(small, -1*num)
        elif len(small) == 1 and len(big) == 0:
            arr = [-1*heapq.heappop(small), num]
            heapq.heappush(small, -1*min(arr))
            heapq.heappush(big, max(arr))
        else:
            print(len(small), len(big))
            if big[0] < num:
                heapq.heappush(big, num)
            else:
                heapq.heappush(small, -1*num)
        # print(small, big)
        if len(big) > len(small):
            if len(small) == 0 and len(big) == 2:
                val = heapq.heappop(big)
                heapq.heappush(small, val)
            elif len(big) > len(small) + 1:
                arr = [heapq.heappop(big), heapq.heappop(big)]
                heapq.heappush(small, -1*min(arr))
                heapq.heappush(big, max(arr))
            elif len(big) > len(small):
                heapq.heappush(small, -1*heapq.heappop(big))
        else:
            if len(big) == 0 and len(small) == 2:
                val = -1*heapq.heappop(small)
                heapq.heappush(big, val)
            elif len(small) >= len(big) + 2:
                arr = [-1*heapq.heappop(small), -1*heapq.heappop(small)]
                heapq.heappush(small, -1*min(arr))
                heapq.heappush(big, max(arr))
        while small and big and big[0] < -1*small[0]:
            entry = big.pop()
            heapq.heappush(small, -1*entry)
            

        # print(small, big)
        res = 0.0
        if len(small) == len(big):
            res = (-1*small[0]+big[0])/2
        else:
            res = -1*small[0]*1.0
        
        values.append(res)
    return values
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = []

    for _ in range(a_count):
        a_item = int(input())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
