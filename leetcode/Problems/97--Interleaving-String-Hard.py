class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:        
        m, n = len(s1), len(s2)
        if len(s3) != m+n:
            return False
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(m):
            dp[i+1][0] = (s1[i]==s3[i]) and dp[i][0]
        for i in range(n):
            dp[0][i+1] = (s2[i]==s3[i]) and dp[0][i]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                    dp[i][j] = True
                if s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                    dp[i][j] = True
        return dp[m][n]