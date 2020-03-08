class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        answer = 0
        val = 0
        
        for ch in S:
            if ch == '(':
                val += 1
            elif ch == ')':
                val -= 1
            
            if val < 0:
                answer += 1
                val += 1
                
        return answer + val
        