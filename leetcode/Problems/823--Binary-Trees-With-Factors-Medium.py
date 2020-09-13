class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A = sorted(A)
        dp, answer, modVal = Counter(), 0, 10**9+7
        factors = defaultdict(set)
        for i in range(len(A)):
            for j in range(i):
                if A[i]%A[j] == 0:
                    factors[A[i]].add(A[j])
        for i in range(len(A)):
            dp[A[i]] = 1
            for factor in factors[A[i]]:
                dp[A[i]] += (dp[factor]*dp[A[i]//factor])
            answer = (answer + dp[A[i]]) %modVal
        return answer%modVal