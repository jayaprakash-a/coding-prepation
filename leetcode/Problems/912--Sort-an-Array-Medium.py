class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        elif len(nums) == 2:
            return [min(nums[0], nums[1]), max(nums[0], nums[1])]
        
        left = self.sortArray(nums[:(len(nums)//2)])
        right = self.sortArray(nums[(len(nums)//2):])
        
        lInd, rInd = 0, 0
        newArr = []
        
        while(lInd < len(left) and rInd < len(right)):
            if left[lInd] < right[rInd]:
                newArr.append(left[lInd])
                lInd += 1
            else:
                newArr.append(right[rInd])
                rInd += 1
                
        while(lInd < len(left)):
            newArr.append(left[lInd])
            lInd += 1
        while(rInd < len(right)):
            newArr.append(right[rInd])
            rInd += 1
            
        
        return newArr
            
        
        