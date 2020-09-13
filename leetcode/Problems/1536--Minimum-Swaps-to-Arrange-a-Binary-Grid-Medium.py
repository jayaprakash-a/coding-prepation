class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        zeroCount = [0]*n
        for i in range(n):
            value = 0
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:                    
                    break
                else:
                    value += 1
            zeroCount[i] = value
        answer = 0
        for i in range(n):            
            if zeroCount[i] >= n-i-1:
                continue
            found = False
            for j in range(i+1, n):
                if zeroCount[j] >= n-i-1:
                    found = True
                    answer += (j-i)
                    zeroCount[i+1:j+1] = zeroCount[i:j]
                    break
            if not found:
                return -1

        return answer