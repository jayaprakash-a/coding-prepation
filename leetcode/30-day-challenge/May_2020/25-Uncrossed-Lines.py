class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for _ in range(len(B)+1)] for _  in range(len(A)+1)]
        answer = 0
        for i1 in range(len(A)):
            for j1 in range(len(B)):
                i = i1 + 1
                j = j1 + 1
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if A[i1] == B[j1]:
                    # print(i, j, A[i1], B[j1])
                    dp[i][j] = max(dp[i-1][j-1] + 1, dp[i][j])
                answer = max(answer, dp[i][j])
        # print(dp)
        return answer