class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer = []
        
        for word in words:
            charMap = {}
            flag = True
            for i in range(len(word)):
                if word[i] not in charMap.keys():
                    if pattern[i] in charMap.values():
                        flag = False
                        break
                    charMap[word[i]] = pattern[i]
                else:
                    if charMap[word[i]] != pattern[i]:
                        flag = False
                        break
            if flag:
                answer.append(word)
        
        return answer
        