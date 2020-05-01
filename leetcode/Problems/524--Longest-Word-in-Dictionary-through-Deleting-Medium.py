class Solution:
    def maxSubSeqLen(self, s, t):
        sLen, tLen = len(s), len(t)
        i, j = 0, 0        
        while(i<sLen and j<tLen):
            if s[i] == t[j]:
                j += 1
            i += 1
        if j == tLen:
            return j
        return 0
    
    def findLongestWord(self, s: str, d: List[str]) -> str:
        maxLen = 0
        maxWord = ''
        for word in d:
            length = self.maxSubSeqLen(s, word)
            # print(length, word)
            if length == maxLen:
                maxWord = min(maxWord, word)                
            elif length > maxLen:
                maxWord = word
                maxLen = length
        return maxWord