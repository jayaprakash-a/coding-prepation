class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, answer, sumVal = 0, len(nums)+2, 0
        for right in range(len(nums)):
            sumVal += nums[right]
            while sumVal >= s:
                answer = min(answer, right-left+1)
                sumVal -= nums[left]
                left += 1
        if answer == len(nums) + 2:
            return 0
        return answer