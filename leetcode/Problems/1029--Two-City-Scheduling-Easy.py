class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        def compare(x):
            return x[0]-x[1]
        costs = sorted(costs, key = compare)
        a, b = len(costs)//2 , len(costs)//2
        answer = 0
        for i in range(len(costs)):
            if a > 0:
                answer += costs[i][0]
                a -= 1
            else:
                answer += costs[i][1]
                b -= 1
        return answer