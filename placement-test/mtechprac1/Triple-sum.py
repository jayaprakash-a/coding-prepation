import math
import os
import random
import re
import sys
import bisect
# Complete the triplets function below.
def triplets(a, b, c):
    a, b, c = list(set(a)), list(set(b)), list(set(c))
    answer = 0
    a, c = sorted(a), sorted(c)
    for num in b:
        aval = bisect.bisect_right(a, num)
        cval = bisect.bisect_right(c, num)
        print(num, aval, cval)
        answer += (aval*cval)
    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
