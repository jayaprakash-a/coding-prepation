class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        answer = [1]*len(nums)
        
        for i in range(1, len(nums)):
            maxVal = 0
            for j in range(i):
                if nums[i] > nums[j] and answer[j] > maxVal:
                    maxVal = answer[j]
            answer[i] = maxVal+1
        
        # print(answer)
        return max(answer)
                    
                    
        