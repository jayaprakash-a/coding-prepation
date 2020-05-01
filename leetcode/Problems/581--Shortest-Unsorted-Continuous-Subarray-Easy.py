class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:      
        n = sorted(nums)
        i = 0
        while(i < len(nums) and nums[i] == n[i]):
            i += 1
        start = i
        if i == len(nums):
            return 0
        i = len(nums)-1
        while(i>=0 and nums[i] == n[i]):
            i -= 1
        return i-start+1