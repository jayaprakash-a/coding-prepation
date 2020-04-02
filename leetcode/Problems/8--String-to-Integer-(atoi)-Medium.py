class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        while(i < len(str) and str[i] == ' '):
            i += 1
        if i == len(str):
            return 0
        if str[i].isdigit() or str[i] == '-' or str[i] == '+':
            pass
        else:
            return 0
        hasDigit = False
        numStr = str[i]
        if str[i].isdigit():
            hasDigit = True
        i += 1
        
        while(i < len(str) and str[i].isdigit()):
            hasDigit = True
            numStr += str[i]
            i += 1
        if not hasDigit:
            return 0
        # if len(numStr) > 11:
        #     if numStr[0] == '-':
        #         return -2147483648
        #     elif numStr[0] == '+':
        #         return 2147483647
        answer = int(numStr)
        minAns = max(answer, -2147483648)
        maxAns = min(answer, 2147483647)
        
        if minAns == maxAns:
            return minAns
        elif maxAns == 2147483647:
            return 2147483647
        else:
            return -2147483648
            
        
        