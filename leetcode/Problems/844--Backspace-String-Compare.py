class Solution:
    def getString(self, S):
        newStr = []
        for ch in S:
            if ch.isalpha():
                newStr += [ch]
            elif ch == '#':
                if len(newStr) > 0:
                    newStr.pop()
        return ''.join(newStr)
    def backspaceCompare(self, S: str, T: str) -> bool:
        sNew = self.getString(S)
        tNew = self.getString(T)
        
        return sNew == tNew
            