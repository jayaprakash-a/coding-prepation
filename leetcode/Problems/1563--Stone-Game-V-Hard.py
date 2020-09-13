class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        preSum = [0]
        for entry in stoneValue:
            preSum.append(preSum[-1] + entry)
        answer = {}
        def helper(i, j):
            if (i, j) in answer:
                return answer[(i, j)]
            result = 0
            for m in range(i, j):
                l, r = preSum[m] - preSum[i], preSum[j] - preSum[m]
                if l >= r:
                    result = max(result, helper(m, j) + r)
                if r >= l:
                    result = max(result, helper(i, m) + l)
            answer[(i, j)] = result
            return result
        
        return helper(0, len(stoneValue))