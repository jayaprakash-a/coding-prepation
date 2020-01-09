class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        maxSumInclusive = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            maxSum = max(num, maxSumInclusive + num, maxSum)
            maxSumInclusive = max(num, maxSumInclusive + num)
        
        return maxSum
        