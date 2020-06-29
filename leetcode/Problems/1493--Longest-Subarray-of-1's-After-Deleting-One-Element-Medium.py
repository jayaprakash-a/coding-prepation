class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        preVals, suffVals = [0]*len(nums), [0]*len(nums)
        for i in range(1, len(nums)):
            if nums[i-1] == 1:
                preVals[i] = preVals[i-1]+1
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1] == 1:
                suffVals[i] = suffVals[i+1]+1
        # print(preVals, suffVals)
        answer = 0
        for i in range(len(nums)):
            answer = max(answer, suffVals[i]+preVals[i])
        return max(answer, max(preVals), max(suffVals))
        