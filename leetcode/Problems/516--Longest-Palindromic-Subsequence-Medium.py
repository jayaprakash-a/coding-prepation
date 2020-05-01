class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) <= 0 or s == s[::-1]:
            return len(s)

        lcs = [[-1 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            for j in range(len(s)+1):
                if i==0 or j==0:
                    lcs[i][j] = 0
                elif s[i-1] == s[-j]:
                    lcs[i][j] = lcs[i-1][j-1]+1
                else:
                    lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
        

        
        return lcs[len(s)][len(s)]