class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = list(str(num))
        numSorted = sorted(numStr, reverse=True)
        index = -1
        for i in range(len(numStr)):
            if numStr[i] != numSorted[i]:
                index = i
                break
        
        if index == -1:
            return num
        maxVal = -1
        maxInd = -1
        for i in range(index+1, len(numStr)):
            if int(numStr[i]) >= maxVal:
                maxVal = int(numStr[i])
                maxInd = i
        
        numStr[maxInd], numStr[index] = numStr[index], numStr[maxInd]
        
        return int(''.join(numStr))
        