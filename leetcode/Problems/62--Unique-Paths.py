class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N, K = m+n-2, min(m-1, n-1)
        # print(N, K)
        numProd, denomProd = 1, 1
        for i in range(1, K+1):
            numProd *= (N-i+1)
            denomProd *= i
        
        return numProd//denomProd
        
        