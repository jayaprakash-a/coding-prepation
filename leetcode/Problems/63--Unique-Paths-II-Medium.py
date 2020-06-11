class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    if i == j == 0:
                        grid[i][j] = 1
                        continue
                    elif i == 0:
                        grid[i][j] = grid[i][j-1]
                        continue
                    elif j == 0:
                        grid[i][j] = grid[i-1][j]
                        continue
                    grid[i][j] = grid[i][j-1] + grid[i-1][j]
                else:
                    grid[i][j] = 0
        return grid[-1][-1]
        
        