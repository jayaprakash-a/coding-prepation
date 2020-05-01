class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxInc = nums[0]
        maxOverall = nums[0]
        for i in range(1, len(nums)):
            maxInc = max(nums[i], nums[i]+maxInc)
            maxOverall = max(maxOverall, maxInc)
        return maxOverall
        