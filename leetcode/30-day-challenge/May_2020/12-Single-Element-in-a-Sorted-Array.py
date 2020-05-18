class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if len(nums) == 1:
            return nums[0]
        mid = 0
        while(l <= r):      
            
            mid = l + (r-l)//2
            # print(l, r, mid)
            if 1 <= mid < len(nums)-1 and nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif mid == len(nums)-1 and nums[mid] != nums[mid-1]:
                return nums[mid]
            elif mid == 0 and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif nums[mid] == nums[mid+1] and mid%2 == 1:
                r = mid-1
            elif nums[mid] == nums[mid+1] and mid%2 == 0:
                l = mid+1
            elif nums[mid] == nums[mid-1] and mid%2 == 0:
                r = mid-1
            elif nums[mid] == nums[mid-1] and mid%2 == 1:
                l = mid+1
        
        return nums[mid]
            
        