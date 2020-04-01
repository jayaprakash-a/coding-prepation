class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch not in magazine:
                return False
            else:
                magazine = magazine.replace(ch, '', 1)
        
        return True
        
        