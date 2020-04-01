class Solution:
    def __init__(self):
        self.result = []
    def genPerm(self, nums, pos):
        if pos == len(nums):
            self.result.append(list(nums))
            return
        for i in range(pos, len(nums)):
            nums[i], nums[pos] = nums[pos], nums[i]
            self.genPerm(nums, pos+1)
            nums[i], nums[pos] = nums[pos], nums[i]
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.genPerm(nums, 0)
        
        return self.result
        