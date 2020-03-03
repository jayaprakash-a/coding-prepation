class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        gridTranspose = []
        
        for j in range(len(grid[0])):
            row = []
            for i in range(len(grid)):
                row.append(grid[i][j])
            gridTranspose.append(row)
        # print(gridTranspose)
        # print(grid)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (sum(grid[i]) >= 2 or sum(gridTranspose[j]) >= 2):
                    # print(i, j, grid[i][j])
                    count += 1
        return count
            
        