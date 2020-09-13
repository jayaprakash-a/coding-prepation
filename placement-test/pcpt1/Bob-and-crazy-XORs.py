import math
import os
import random
import re
import sys
class TrieNode:    
    def __init__(self):
        self.children = [None for _ in range(2)]
        self.value = 0

def insert(root, number):
    temp = root
    binRep = bin(number)[2:].zfill(32)
    for ch in binRep:
        ch = int(ch)
        if temp.children[ch] == None:
            temp.children[ch] = TrieNode()
        temp = temp.children[ch]
    temp.value = number

def getMax(root, number):
    temp = root
    binRep = bin(number)[2:].zfill(32)
    traversed = 0
    start = 1<<31
    for ch in binRep:
        ch = int(ch)
        if temp.children[1-ch] != None:
            if ch == 0:
                traversed |= start
            temp = temp.children[1-ch]
        elif temp.children[ch] != None:
            if ch == 1:
                traversed |= start
            temp = temp.children[ch]
        else:
            return traversed^number
        start >>= 1
    return temp.value^number
def solve(n, a, x):
    numReps = TrieNode()
    for num in a:
        insert(numReps, num)
    answer = []
    for num in x:
        answer.append(getMax(numReps,num))
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    q = int(input().strip())

    x = []

    for _ in range(q):
        x_item = int(input().strip())
        x.append(x_item)

    result = solve(n, a, x)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
