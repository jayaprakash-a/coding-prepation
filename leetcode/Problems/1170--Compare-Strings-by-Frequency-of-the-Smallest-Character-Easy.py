class Solution:
    def getFrequency(self, words):
        freqVal = []
        for word in words:
            charCount = [0]*26
            for ch in word:
                charCount[ord(ch)-ord('a')] += 1
            i = 0
            while(charCount[i] == 0):
                i += 1
            freqVal.append(charCount[i])
        return freqVal
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        queryVal = self.getFrequency(queries)
        wordVal = self.getFrequency(words)
        # print(queryVal, wordVal)
        answer = []
        for num in queryVal:
            count = 0
            for val in wordVal:
                if num < val:
                    count += 1
            answer.append(count)
        
        return answer
            
        
        