class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        wordMap = {}
        words =  str.split(' ')
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in wordMap.keys():
                if words[i] in wordMap.values():
                    return False
                wordMap[pattern[i]] = words[i]
            elif pattern[i] in wordMap.keys():
                if wordMap[pattern[i]] != words[i]:
                    return False
        return True
        