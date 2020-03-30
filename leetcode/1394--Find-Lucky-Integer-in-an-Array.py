class Solution:
    def findLucky(self, arr: List[int]) -> int:
        numCount = {}
        for num in arr:
            if num in numCount.keys():
                numCount[num] += 1 
            else:
                numCount[num] = 1
        
        keySorted = sorted(numCount.keys(), reverse=True)
        
        for key in keySorted:
            if numCount[key] == key:
                return key
        
        return -1
        