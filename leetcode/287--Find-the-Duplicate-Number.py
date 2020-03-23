class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        prev = -1
        
        for i in range(len(nums)):
            if nums[i] == prev:
                return prev
            prev = nums[i]
        
        return prev
        