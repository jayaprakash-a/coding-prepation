class Solution:
    def minInsertions(self, s: str) -> int:
        string = s
        revString = s[::-1]
        lcs = [[None]*(len(s)+1) for i in range(len(s)+1)]
        for i in range(len(s) + 1):
            for j in range(len(s) + 1):
                if i == 0 or j == 0:
                    lcs[i][j] = 0
                elif string[i-1] == revString[j-1]:
                    lcs[i][j] = lcs[i-1][j-1]+1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
        lcsVal = lcs[-1][-1]
        # print(lcsVal)
        
        return len(s) - lcsVal
                    
            