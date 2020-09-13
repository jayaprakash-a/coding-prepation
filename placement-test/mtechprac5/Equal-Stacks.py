#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    h1sum, h2sum, h3sum = sum(h1), sum(h2), sum(h3)
    # print(h1sum, h2sum, h3sum)
    h1, h2, h3 = h1[::-1], h2[::-1], h3[::-1]
    # print((h1sum != h2sum or h2sum != h3sum or h1sum != h3sum), h1, h2, h3)
    while (h1sum != h2sum or h2sum != h3sum or h1sum != h3sum) and h1 and h2 and h3:
        if h1sum >= h2sum and h1sum >= h3sum:
            h1sum -= h1.pop()
        elif h2sum >= h1sum and h2sum >= h3sum:
            h2sum -= h2.pop()
        elif h3sum >= h2sum and h3sum >= h1sum:
            h3sum -= h3.pop()
    # print(h1sum, h2sum, h3sum)
    return min(h1sum, h2sum, h3sum)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
