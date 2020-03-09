class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        numSum = 0
        lightSum = 0
        count = 0
        allVisit = False
        for i in range(len(light)):
            numSum += i+1
            lightSum += light[i]
            
            if allVisit and light[i] == i+1:
                count += 1
                allVisit = True
                continue
            else:
                allVisit = False
                
            if numSum == lightSum:
                count += 1
                allVisit = True
            else:
                allVisit = False
        
        return count
            
        