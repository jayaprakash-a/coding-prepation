import math
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        prev, count = 0, 0
        
        for num in arr:
            if num == prev:
                count += 1
                if count > math.ceil(0.25*len(arr)):
                    return num
            else:
                prev = num
                count = 1
        
        return arr[-1]
        