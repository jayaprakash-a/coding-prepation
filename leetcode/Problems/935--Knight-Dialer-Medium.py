class Solution:
    def knightDialer(self, N: int) -> int:
        posMoves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        
        
        dp = [0]*10
        newDp = [0]*10
        for i in range(N):
            for j in range(10):
                newDp[j] = dp[j]
                dp[j] = 0
            for j in range(10):
                if i == 0:
                    dp[j] = 1
                else:                    
                    for k in posMoves[j]:
                        dp[j] += newDp[k]

        answer, modVal = 0, 10**9+7
        for j in range(10):
            answer = (answer + dp[j])%modVal
        return answer