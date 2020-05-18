class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def maxSubArray(nums: List[int]) -> int:
            maxInc = nums[0]
            maxOverall = nums[0]
            for i in range(1, len(nums)):
                maxInc = max(nums[i], nums[i]+maxInc)
                maxOverall = max(maxOverall, maxInc)
            return maxOverall
        def minSubArray(nums: List[int]) -> int:
            minInc = nums[0]
            minOverall = nums[0]
            for i in range(1, len(nums)):
                minInc = min(nums[i], nums[i]+minInc)
                minOverall = min(minOverall, minInc)
            return minOverall
        sumVal = sum(A)
        minSubSum = minSubArray(A)
        maxSubSum = maxSubArray(A)
        maxVal = max(A)
        if sumVal-minSubSum == 0:
            return max(maxVal, maxSubSum)
        return max(maxSubSum, sumVal - minSubSum, maxVal)