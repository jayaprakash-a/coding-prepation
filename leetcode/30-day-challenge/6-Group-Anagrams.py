class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordGroup = {}
        answer = []
        for string in strs:
            newStr = ''.join(list(sorted(string)))
            if newStr not in wordGroup.keys():
                wordGroup[newStr] = [string]
            else:
                wordGroup[newStr] += [string]
        
        for word in wordGroup.keys():
            answer += [wordGroup[word]]
            
        return answer
        