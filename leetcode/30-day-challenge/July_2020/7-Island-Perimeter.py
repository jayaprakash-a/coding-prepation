class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].insert(0, 0)
            grid[i].append(0)
        grid.append([0 for _ in range(len(grid[0]))])
        grid.insert(0, [0 for _ in range(len(grid[0]))])
        answer = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 1:
                    answer += (4 - grid[i-1][j] - grid[i+1][j] - grid[i][j-1] - grid[i][j+1])
        return answer