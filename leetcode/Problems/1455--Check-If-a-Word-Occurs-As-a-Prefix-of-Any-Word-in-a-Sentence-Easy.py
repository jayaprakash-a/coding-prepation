class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        split = sentence.split(' ')
        for i in range(len(split)):
            word = split[i]
            if word[:len(searchWord)] == searchWord:
                return i+1
        return -1