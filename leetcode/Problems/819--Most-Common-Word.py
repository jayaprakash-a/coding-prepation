class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        
        wordCount = {}
        maxVal, maxWord = 0, ''
        for word in words:
            if word not in banned:
                if word not in wordCount.keys():
                    wordCount[word] = 1
                else:
                    wordCount[word] += 1
                if wordCount[word] > maxVal:
                    maxVal = wordCount[word]
                    maxWord = word
        return maxWord
        
                    
                