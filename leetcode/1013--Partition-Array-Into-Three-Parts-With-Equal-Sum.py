class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sumVal = 0
        for num in A:
            sumVal += num
        
        count = 0
        newSum = 0
        if sumVal%3 != 0:
            return False
        for num in A:
            newSum += num
            if newSum == sumVal//3:
                count += 1
                newSum = 0
                if count == 3:
                    return True
        
            
        