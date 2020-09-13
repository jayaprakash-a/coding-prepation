class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        answer, i = 0, 0
        while i < len(s) - 1:            
            if s[i] == s[i+1]:
                answer += min(cost[i], cost[i+1])
                cost[i+1] = max(cost[i], cost[i+1])
            i += 1
            
        return answer
            
        