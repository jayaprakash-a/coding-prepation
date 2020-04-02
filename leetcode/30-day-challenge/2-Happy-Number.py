class Solution:
    def isHappy(self, n: int) -> bool:
        possibleNums = set()
        
        while(True):
            newNum = 0
            for ch in str(n):
                newNum += (int(ch)**2)
            strNum = sorted(str(newNum))
            strNum = ''.join(strNum)
            if strNum in possibleNums:
                return False
            else:
                possibleNums.add(strNum)
            if newNum == 1:
                return True
            n = newNum
                
            