class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) <= 2:
            return max(nums)

        nums = sorted(list(set(nums)), reverse=True)
        return nums[2]
