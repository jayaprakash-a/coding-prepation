class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tc = Counter(t)
        for ch in s:
            tc[ch] -= 1
        
        for ch in tc:
            if tc[ch] == 1:
                return ch