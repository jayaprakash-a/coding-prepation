class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ['(', '{', '[']
        closeBrackets = [')', '}', ']']
        container = ""
        for ch in s:
            if ch in openBrackets:
                container += ch
            elif ch in closeBrackets:
                if len(container) == 0:
                    return False
                matchBracket = container[-1]
                container = container[:-1]
                if openBrackets.index(matchBracket) != closeBrackets.index(ch):
                    return False
        if len(container) == 0:
            return True
        else:
            return False
                        
                
            
        