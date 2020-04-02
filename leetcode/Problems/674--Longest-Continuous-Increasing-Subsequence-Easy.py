class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxLen, currLen = 0, 1
        if len(nums) <= 1:
            return len(nums)
        
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                currLen += 1
            else:
                if currLen > maxLen:
                    maxLen = currLen
                currLen = 1
        if currLen > maxLen:
            maxLen = currLen
        return maxLen