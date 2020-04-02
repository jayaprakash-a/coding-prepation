class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxLen = 0 
        
        try:
            char = strs[0][0]
            for j in range(len(strs[0])):
                char = strs[0][j]         
                for i in range(len(strs)):
                    if strs[i][j] != char:
                        return strs[0][:maxLen]
                maxLen += 1
        except :
            pass
        try:
            return strs[0][:maxLen]
        except:
            return ""
            