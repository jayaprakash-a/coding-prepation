class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxVal = max(nums)
        
        values = [0]*maxVal
        
        for num in nums:
            values[num-1] += num
        
        if len(values) == 0:
            return 0
        if len(values) <= 2:
            return max(values)
        
        solution = [values[0], max(values[0], values[1])]
        
        for i in range(2, len(values)):
            answer = max(solution[i-2]+values[i], solution[i-1])
            solution.append(answer)
        return solution[-1]
        