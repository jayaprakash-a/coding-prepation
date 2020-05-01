class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            
            for i in (1, -1):
                dfs(row+i, col)
                dfs(row,  col+i)

        
        
        answer = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    answer += 1
                    dfs(i, j)
        return answer