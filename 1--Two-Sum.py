class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i  in range (len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return i,j
        original = nums
        nums = sorted(nums)
        left, right = 0, len(nums) - 1
        while(nums[left]+nums[right] != target):
            sum = nums[left]+nums[right]
            if sum > target:
                right -= 1
            else:
                left += 1
        
        leftIndex, rightIndex = 0, 0
        
        for i in range(len(original)):
            if original[i] == nums[left]:
                leftIndex = i
        for i in range(len(original)):
            if original[i] == nums[right] and i != leftIndex:
                rightIndex = i
        
        return leftIndex, rightIndex
        
            
        