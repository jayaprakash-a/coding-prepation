class Solution:
    def isHappy(self, n: int) -> bool:
        numStr = str(n)
        numberList = []
        
        while(True):
            sum = 0
            for ch in numStr:
                sum += (int(ch)**2)
            if sum == 1:
                return True
            elif sum in numberList:
                return False
            else:
                numberList.append(sum)
            numStr = str(sum)
        
        return 
                
        