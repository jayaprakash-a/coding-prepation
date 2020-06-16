class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumVal = sum(nums)
        
        if sumVal % 2 == 1:
            return False
        
        posSum, sumVal = {0}, sumVal>>1
        
        for num in nums:
            posSum |= {v + num for v in posSum}
            if sumVal in posSum:
                return True
        return False