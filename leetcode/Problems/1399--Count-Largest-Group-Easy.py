class Solution:
    def countLargestGroup(self, n: int) -> int:
        sumDict = {}
        maxVal = 1
        for i in range(1, n+1):
            sumVal = 0
            for ch in str(i):
                sumVal += int(ch)
            if sumVal not in sumDict.keys():
                sumDict[sumVal] = 1
            else:
                sumDict[sumVal] += 1
                if sumDict[sumVal] > maxVal:
                    maxVal = sumDict[sumVal]
        count = 0
        for key in sumDict.keys():
            if sumDict[key] == maxVal:
                count += 1
        return count
