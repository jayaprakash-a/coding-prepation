class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] > nums[high]:
                low = mid+1
            elif nums[mid] < nums[low]:
                high = mid
                low += 1
            else:
                high -= 1
        
        return nums[low]