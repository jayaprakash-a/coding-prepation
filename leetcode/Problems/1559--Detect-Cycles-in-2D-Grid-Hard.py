class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # print('----------------')
        visited = set()
        m, n = len(grid), len(grid[0])
        def getComp(dir):
            if dir == (0, 1):
                return (0, -1)
            if dir == (0, -1):
                return (0, 1)
            if dir == (1, 0):
                return (-1, 0)
            if dir == (-1, 0):
                return (1, 0)
        def helper(i, j, ch, dirs):
            # print(i, j, ch)             
            for dir in dirs:
                newI, newJ = i+dir[0], j+dir[1]
                if 0 <= newI < m and 0 <= newJ < n:                    
                    if (newI, newJ) in visited:
                        # print(newI, newJ, visited)
                        return True
                    if grid[newI][newJ] == ch:
                        grid[newI][newJ] = '#'
                        visited.add((newI, newJ))
                        # print('COMP', dir, direction - set([getComp(dir)]))
                        if helper(newI, newJ, ch, direction - set([getComp(dir)])):
                            return True
                    
            
            
        direction = set([(0, 1), (0, -1), (1, 0), (-1, 0)])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '#':
                    continue
                temp = grid[i][j]
                grid[i][j] = '#'
                answer = helper(i, j, temp, direction)
                visited.add((i, j))
                if answer:
                    return True
                visited = set()
                #grid[i][j] = temp
        return False
        
                    