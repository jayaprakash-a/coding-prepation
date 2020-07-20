#!/bin/python3

import math
import os
import random
import re
import sys
def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True

    if (n % 2 == 0 or n % 3 == 0) : 
        return False  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
    
def solve(primes, N):
    if N <= 3:
        return 'Redraw'
    sqrt = math.sqrt(N)
    if int(sqrt)**2 == N:
        return 'Earth'
    if primes[N]:            
        return 'Redraw'    
    return 'Nibieru'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())
    nums = []
    for T_itr in range(T):
        N = int(input().strip())
        nums.append(N)
    maxVal = max(nums)
    primes = [True for i in range(maxVal + 1)] 
    p = 2
    while (p * p <= maxVal):           
        if (primes[p] == True):               
            for i in range(p * 2, maxVal + 1, p): 
                primes[i] = False
        p += 1
    primes[0]= False
    primes[1]= False
    for num in nums:
        result = solve(primes, num)

        fptr.write(result + '\n')

    fptr.close()
