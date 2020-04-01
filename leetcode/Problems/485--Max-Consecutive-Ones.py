class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxVal = 0
        curCount = 0
        
        for num in nums:
            if num == 0:
                curCount = 0
            else:
                curCount += 1
                if curCount > maxVal:
                    maxVal = curCount
        
        return maxVal
        