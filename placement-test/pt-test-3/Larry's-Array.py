#!/bin/python3

import math
import os
import random
import re
import sys

def larrysArray(A):
    def merge(left, mid, right):
        i, j, k, inversions = left, mid+1, 0, 0
        tempArray = [0]*(right-left+1)
        while i <= mid and j <= right:
            if A[i] <= A[j]:
                tempArray[k] = A[i]
                k += 1
                i += 1
            else:
                inversions += (mid-i+1)
                tempArray[k] = A[j]
                k += 1
                j += 1
        while i <= mid:
            tempArray[k] = A[i]
            k += 1
            i += 1
        while j <= right:
            tempArray[k] = A[j]
            k += 1
            j += 1
        for i in range(left, right+1):
            A[i] = tempArray[i-left]
        return inversions
    def mergeSort(left, right):
        inversions = 0
        if left < right:
            mid = (left+right)//2
            inversions += mergeSort(left, mid)
            inversions += mergeSort(mid+1, right)
            inversions += merge(left, mid, right)
        return inversions
    
    inversions = mergeSort(0, len(A)-1)
    # print(inversions, A)
    if inversions % 2 == 0:
        return 'YES'            
    return 'NO'
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
