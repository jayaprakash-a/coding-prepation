class Solution:
    def isSubsequence(self, word1: str, word2: str) -> bool:
        j = 0 
        if len(word1) == 0:
            return True
        for i in range(len(word2)):
            if word2[i] == word1[j]:
                j += 1
            if j == len(word1):
                return True
        return False