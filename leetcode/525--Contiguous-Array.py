class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, maxVal = 0, 0
        numSet = {}
        numSet[0] = -1
        
        for i in range(len(nums)):
            num = nums[i]
            if num == 0:
                zero += 1
            else:
                zero -= 1
            if zero in numSet.keys() and (i-numSet[zero]) > maxVal:
                maxVal = i-numSet[zero]
                
            elif zero not in numSet.keys():
                numSet[zero] = i
        # print(numSet)
        return maxVal
            