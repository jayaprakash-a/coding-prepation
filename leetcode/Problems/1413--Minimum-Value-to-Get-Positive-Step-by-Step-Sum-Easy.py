class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minSum = nums[0]
        sum = nums[0]
        for num in nums[1:]:
            sum += num
            minSum = min(minSum, sum)

        # if minSum >= 1:
        #     return 1
        return max(1, 1-minSum)
