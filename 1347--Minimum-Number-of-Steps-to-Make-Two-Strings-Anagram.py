class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if s == t or len(s) == 0:
            return 0
        count = 0

        charCount = [0] * 26

        for i in range(26): 
            charCount[i] = 0
            
        for i in range(len( s)):  
            charCount[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):  
            charCount[ord(t[i]) - ord('a')] -= 1
            if (charCount[ord(t[i]) - ord('a')] < 0) : 
                count += 1

        return count 
        
        

        
        