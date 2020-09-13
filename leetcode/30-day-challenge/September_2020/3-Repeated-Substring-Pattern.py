class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        for i in range(1, len(s)//2+1):
            new = s[:i]
            if new*(len(s)//len(new)) == s:
                return True
        return False