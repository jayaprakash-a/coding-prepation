class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if len(A) == 1:
            return min(A[0])
        for i in range(1, len(A)):
            for j in range(len(A[i])):
                minVal = min(A[i-1][max(0, j-1)], A[i-1][j], A[i-1][min(j+1, len(A[i])-1)])
                A[i][j] += minVal
        
        return min(A[-1])
                