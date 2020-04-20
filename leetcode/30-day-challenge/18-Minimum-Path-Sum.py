class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        answer = []
        
        for i in range(len(grid)):
            answer.append([-1]*len(grid[0]))
            
        answer[0][0] = grid[0][0]
        
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                minVal = -1 
                if i >=0 and i< m and j-1 >= 0 and j-1 < n:
                    minVal = answer[i][j-1]
                if i-1 >=0 and i-1< m and j >= 0 and j < n:
                    if minVal != -1 and answer[i-1][j] < minVal:
                        minVal = answer[i-1][j]
                    if minVal == -1:
                        minVal = answer[i-1][j]
                        
                    
                if minVal != -1:
                    # minVal = min(arr)
                    answer[i][j] = minVal + grid[i][j]
        
        return answer[m-1][n-1]