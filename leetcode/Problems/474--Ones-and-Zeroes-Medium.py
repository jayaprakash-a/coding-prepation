class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for word in strs:
            one, zero = word.count('1'), word.count('0')
            # one, zero = 0, 0
            # for ch in word:
            #     if ch == '1':
            #         one += 1
            #     else:
            #         zero += 1
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i >= zero and j >= one:
                        dp[i][j] = max(dp[i-zero][j-one]+1, dp[i][j])
        return dp[m][n]
        
