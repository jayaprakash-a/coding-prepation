class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numDict = {}
        
        for num in arr:
            if num not in numDict.keys():
                numDict[num] = 1
            else:
                numDict[num] += 1
                
        return len(numDict.values()) == len(set(numDict.values()))
        