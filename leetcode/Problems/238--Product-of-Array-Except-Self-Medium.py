class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prev = 1
        
        for num in nums:            
            answer.append(prev)
            prev *= num
        
        prev = 1
        
        for i in range(len(nums)-1,-1,-1):
            temp = nums[i]
            nums[i] = prev
            prev *= temp
        
        for i in range(len(nums)):
            answer[i] *= nums[i]
        
        return answer