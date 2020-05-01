class Solution:
    def checkValidString(self, s: str) -> bool:
        a, b, c = 0, 0, 0
        
        for ch in s:
            if ch == '(':
                a += 1
            elif ch == '*':
                b += 1
            else:
                c += 1
            if c > (a+b):
                return False
        
        a, b, c = 0, 0, 0
        
        for ch in s[::-1]:
            if ch == '(':
                a += 1
            elif ch == '*':
                b += 1
            else:
                c += 1
            if a > (c+b):
                return False
        return True
        