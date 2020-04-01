class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            answer = answer ^ (i+1)
            answer = answer ^ nums[i]
        # for i in nums:
            
        return answer