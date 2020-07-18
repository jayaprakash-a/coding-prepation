class Solution:
    def decodeString(self, s: str) -> str:
        charStack = []
        numStack = []
        isDigit = False
        if len(s) == 0:
            return s
        for ch in s:
            if ch.isdigit():
                if isDigit:
                    numStack[-1] = numStack[-1]*10 + int(ch)
                else:
                    numStack.append(int(ch))
                    isDigit = True
            else:
                isDigit = False
                if ch == '[':
                    charStack.append('')
                elif ch == ']':
                    newStr = charStack.pop()*numStack.pop()
                    if len(charStack) == 0:
                        charStack.append('')
                    charStack[-1] += newStr
                else:
                    if len(charStack) == 0:
                        charStack.append('')
                    charStack[-1] += ch        
        return charStack[0]