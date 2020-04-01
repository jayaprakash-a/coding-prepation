class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer, value = 0, 0
        for ch in s:
            if ch == 'R':
                value += 1
            else:
                value -= 1
            
            if value == 0:
                answer += 1
        
        return answer
        