class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowWise, columnWise = [], []
        for i in range(len(grid)):
            rowWise.append(max(grid[i]))
        for i in range(len(grid[0])):
            line = [row[i] for row in grid]
            columnWise.append(max(line))
        maxSum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                posVal = min(rowWise[i], columnWise[j])
                maxSum += posVal - grid[i][j]
        return maxSum
                