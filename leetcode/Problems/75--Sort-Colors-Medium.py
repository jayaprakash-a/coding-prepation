class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l, r, i = 0, len(nums)-1, 0
        
        while i < len(nums):
            # print('start', nums, i, l, r)
            if nums[i] == 0 and i > l:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                # i -= 1
            elif nums[i] == 2 and i < r :
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                # i -= 1
            else:
                i += 1
            # print('end', nums, i, l, r)