class Solution:
    def titleToNumber(self, s: str) -> int:
        answer = 0
        for ch in s:
            answer = 26*answer + (ord(ch)-ord('A')+1)
        return answer