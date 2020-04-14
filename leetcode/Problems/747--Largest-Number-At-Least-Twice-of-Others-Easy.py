class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)-1
        maxVal = max(nums)
        maxIndex = nums.index(maxVal)
        nums.remove(maxVal)
        
        nextMax = max(nums)
        
        if maxVal >= 2*nextMax:
            return maxIndex
        return -1
        