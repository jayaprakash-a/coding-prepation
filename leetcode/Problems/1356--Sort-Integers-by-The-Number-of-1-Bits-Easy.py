class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        numDict = {}
        answer = []
        for num in arr:
            count = str(bin(num)).count('1')
            if count not in numDict.keys():
                numDict[count] = [num]
            else:
                numDict[count].append(num)
        
        for key in sorted(numDict.keys()):
            answer += sorted(numDict[key])
            
        return answer