class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while(left <= right):
            print(left, right)
            if target > nums[right]:
                return right + 1
            if target < nums[left]:
                return left
            
            midIndex = (left+right)//2
            
            if target > nums[midIndex]:
                left = midIndex+1
            elif target < nums[midIndex]:
                right = midIndex-1
            else:
                return midIndex
        
        return None
        