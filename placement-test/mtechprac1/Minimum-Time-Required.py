import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    left, right = 0, min(machines)*goal
    answer = right
    while left <= right:
        mid = (left+right)//2
        count = 0
        for num in machines:
            count += (mid//num)
        if count >= goal:
            answer = min(answer, mid)
            right = mid-1
        else:
            left = mid+1
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
