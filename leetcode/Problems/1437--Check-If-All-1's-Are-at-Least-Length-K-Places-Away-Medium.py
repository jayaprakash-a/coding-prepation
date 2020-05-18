class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        
        dist, index = k, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                index = i
                break
        
        for i in range(index+1, len(nums)):
            # print(i, nums[i], dist)
            if nums[i] == 1 and dist <= 0:
                dist = k
                continue
            elif nums[i] == 1:
                return False
            
            else:
                dist -= 1
        return True