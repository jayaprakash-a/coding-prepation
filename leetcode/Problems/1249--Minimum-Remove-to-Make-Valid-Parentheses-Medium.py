class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        charList = []
        value = 0
        for ch in s:
            if ch.isalpha():
                charList.append(ch)
            elif ch == ')' and value > 0:
                charList.append(ch)
                value -= 1
            elif ch == '(':
                charList.append(ch)
                value += 1
        if value == 0:
            return ''.join(charList)
        for i in range(len(charList)-1, -1, -1):
            if value == 0:
                break
            if charList[i] == '(':
                charList[i] = ''
                value -= 1
        return ''.join(charList)