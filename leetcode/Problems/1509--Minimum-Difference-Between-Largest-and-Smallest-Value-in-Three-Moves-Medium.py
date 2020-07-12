class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) <= 4:
            return 0
        answer = min(nums[-4] - nums[0], nums[-3] - nums[1], nums[-2] - nums[2], nums[-1]-nums[3])
        return answer