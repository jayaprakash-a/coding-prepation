import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        count = 0
        numList = [True]*(n-1)
        numList[0] = False
        numList[1] = True
        
        answer = n-2
        for i in range(2, math.ceil(math.sqrt(len(numList)))+1):
            if numList[i-1]:
                for j in range(2*i, len(numList)+1, i):
                    # if numList[j-1]:
                    numList[j-1] = False
                        # answer -= 1
        
        # print(numList)
        # return answer
        return numList.count(True)