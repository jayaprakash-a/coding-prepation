class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        while(left < len(nums) and right < len(nums)):
            while(right < len(nums) and nums[right] == 0):
                right += 1
            while(left < len(nums) and nums[left] != 0):
                left += 1
            if left >= len(nums) or right >= len(nums):
                break
            if left >= right:
                right = left+1
                continue
            nums[right], nums[left] = nums[left], nums[right]
            
        
        