class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer, i, j = 0, 0, len(grid[0])-1
        rowLength = len(grid[0])
        while(i < len(grid)):
            while(grid[i][j] < 0 and j >= 0):
                j -= 1
            # print(rowLength-j-1, j)
            answer += (rowLength-j-1)
            i += 1
        return answer