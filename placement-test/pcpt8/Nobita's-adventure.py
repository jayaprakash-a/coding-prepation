from collections import *
def getAns(arr):
    sameIndex = defaultdict(list)
    visited = [-1 for _ in range(len(arr))]
    q = deque()
    q.append(0)

    for i in range(len(arr)):
        sameIndex[arr[i]].append(i)
    visited[0] = 0
    while q:
        index = q.popleft()        
        valid = sameIndex[arr[index]]
        if index > 0:
            valid.append(index-1)
        if index < len(arr)-1:
            valid.append(index+1)
        while valid:
            entry = valid.pop()
            if entry != index and visited[entry] == -1:
                visited[entry] = visited[index]+1
                q.append(entry)
            if entry == len(arr) - 1:
                return visited[-1]
n = int(input())
arr = list(map(int, input().split()))
print(getAns(arr))