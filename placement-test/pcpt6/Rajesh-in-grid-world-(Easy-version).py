import collections
import sys
def getAns(grid):
    penalty = {}
    start = [0, 0]
    end = [0, 0]
    n, m = len(grid), len(grid[0])
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == -2:
                start = [i, j]
                count += 1
            if grid[i][j] == -3:
                end = [i, j]
                count += 1
            if count == 2:
                break
        if count == 2:
            break
    penalty[tuple(start)] = 0
    neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    nodes = collections.deque([[(start[0], start[1]), 0]])
    
    def valid(node):
        return 0 <= node[0] < n and 0 <= node[1] < m and grid[node[0]][node[1]] != -1
    
    
    addedVertices = set()
    addedVertices.add(tuple(start))
    while len(penalty) < n*m  and len(nodes) > 0:
        node = nodes.popleft()
        addedVertices.remove(node[0])
        score = penalty[node[0]]
        # print(node[0], score)
        for adj in neighbours:
            newNode = (adj[0]+node[0][0], adj[1]+node[0][1])                   
            if valid(newNode):
                newScore = score + 1
                if grid[newNode[0]][newNode[1]] != -3:
                    newScore += grid[newNode[0]][newNode[1]]
                if newNode not in penalty:  
                    penalty[newNode] = newScore
                    if newNode not in addedVertices:
                        nodes.append([newNode, score + 1])
                        addedVertices.add(newNode)
                elif penalty[newNode] > newScore:
                    penalty[newNode] = newScore
                    
                    if newNode not in addedVertices:
                        nodes.append([newNode, score + 1])
                        addedVertices.add(newNode)
                
        # print(penalty, addedVertices, newNode)
            # print(nodes)    
    if tuple(end) in penalty:
        return penalty[tuple(end)]
    return -1
    
                
                
    
def main():
    [n, m] = list(map(int, input().strip().split()))
    grid = []
    for _ in range(n):
        arr = list(map(int, input().strip().split()))
        grid.append(arr)
    
    print(getAns(grid))
main()