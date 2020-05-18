class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        first, second = 0, 0
        nums = [float('inf')] + nums + [float('inf')]
        for i in range(1, len(nums)-1, 2):
            first += max(0, nums[i] - min(nums[i-1], nums[i+1])+1)
        for i in range(2, len(nums)-1, 2):
            second += max(0, nums[i] - min(nums[i-1], nums[i+1])+1)
        
        return min(first, second)
        
    