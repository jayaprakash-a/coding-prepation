class Solution:

            
    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            return 0
        if s == s[::-1]:
            return 1
        
        count = 0
        if 'a' in s:
            count += 1
        if 'b' in s:
            count += 1
        
        
        return count
        
        