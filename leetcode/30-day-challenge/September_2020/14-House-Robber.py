class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        valMax = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):           
            maxVal = max(valMax[i-2]+nums[i], valMax[i-1])
            valMax.append(maxVal)
            # print(i, valIncl, valMax)
            
        return valMax[-1]