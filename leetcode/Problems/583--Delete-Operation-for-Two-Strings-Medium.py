class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        lcs = [[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if i==0 or j==0:
                    lcs[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1]+1
                else:
                    lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])        
        return lcs[len(text1)][len(text2)]
    
    def minDistance(self, word1: str, word2: str) -> int:
        maxLen = self.longestCommonSubsequence(word1, word2)
        
        return len(word1)+len(word2)-(2*maxLen)