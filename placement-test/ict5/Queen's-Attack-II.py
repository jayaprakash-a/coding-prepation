#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    blocked = []
    answer = 0
    left, right, top, bottom, diag1, diag2, diag3, diag4 = [], [], [], [], [], [], [], []
    for [x, y] in obstacles:
        print(x, y, r_q, c_q)
        if y == c_q:
            if x > r_q:
                if len(right) == 0:
                    right = [x, y]
                else:
                    if abs(right[0]-r_q) > abs(x-r_q):
                        right = [x, y]
            else:
                if len(left) == 0:
                    left = [x, y]
                else:
                    if abs(left[0]-r_q) > abs(x-r_q):
                        left = [x, y]
        elif x == r_q:
            if y < c_q:
                if len(top) == 0:
                    top = [x, y]
                else:
                    if abs(top[1]-c_q) > abs(y-c_q):
                        top = [x, y]
            else:
                if len(bottom) == 0:
                    bottom = [x, y]
                else:
                    if abs(bottom[1]-c_q) > abs(y-c_q):
                        bottom = [x, y]
        elif x-r_q == y-c_q:
            if x < r_q:
                if len(diag1) == 0:
                    diag1 = [x, y]
                else:
                    if abs(diag1[0]-r_q) > abs(x-r_q):
                        diag1 = [x, y]
            else:
                if len(diag2) == 0:
                    diag2 = [x, y]
                else:
                    if abs(diag2[0]-r_q) > abs(x-r_q):
                        diag2 = [x, y]
        elif x+y == r_q+c_q:
            if x < r_q:
                if len(diag3) == 0:
                    diag3 = [x, y]
                else:
                    if abs(diag3[0]-r_q) > abs(x-r_q):
                        diag3 = [x, y]
            else:
                if len(diag4) == 0:
                    diag4 = [x, y]
                else:
                    if abs(diag4[0]-r_q) > abs(x-r_q):
                        diag4 = [x, y]
    print(left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    if len(left) == 0:
        answer += (r_q-1)
        print('left', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    else:
        answer += (abs(r_q-left[0])-1)
        print('left', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    if len(right) == 0:
        answer += (n-r_q)
        print('right', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    else:
        answer += (abs(r_q-right[0])-1)
        print('right', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    
    if len(top) == 0:
        answer += (c_q-1)
        print('top', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    else:
        answer += (abs(c_q-top[1])-1)
        print('top', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    if len(bottom) == 0:
        answer += (n-c_q)
        print('bottom', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    else:
        answer += (abs(c_q-bottom[1])-1)
        print('bottom', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    
    if len(diag1) == 0:
        answer += (min(r_q, c_q)-1)
        print('diag1', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    else:
        answer += (abs(c_q-diag1[1])-1)
        print('diag1', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    
    if len(diag2) == 0:
        answer += (n - max(r_q, c_q))
        print('diag2', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    else:
        answer += (abs(c_q-diag2[1])-1)
        print('diag2', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
        
    if len(diag3) == 0:
        answer += (min(r_q-1, n-c_q))
        print('diag3', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    else:
        answer += (abs(c_q-diag3[1])-1)
        print('diag3', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    
    if len(diag4) == 0:
        answer += (n - max(r_q, n-c_q))
        print('diag4', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    else:
        answer += (abs(c_q-diag4[1])-1)
        print('diag4', left, right, top, bottom, diag1, diag2, diag3, diag4, answer)
    
        
        
        
        
    return answer
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
