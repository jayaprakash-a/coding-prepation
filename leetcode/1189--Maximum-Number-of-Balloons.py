class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charCount = [0]*(26)
        
        for ch in text:
            charCount[ord(ch)-ord('a')] += 1
        
        
        return min(charCount[0], charCount[1], charCount[11]//2, charCount[14]//2, charCount[13])
        