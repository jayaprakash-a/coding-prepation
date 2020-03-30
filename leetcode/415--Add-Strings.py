class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        carry = 0
        answer = ''
        diff = len(num1)-len(num2)
        for i in range(len(num2)-1, -1, -1):
            sum = (ord(num2[i])-ord('0')) + (ord(num1[i+diff])-ord('0')) + carry
            answer += chr(sum%10 + ord('0'))
            carry = sum//10
        # print(carry, answer[::-1], 'trial1')
        newAns = ''
        for i in range(diff-1, -1, -1):
            sum = (ord(num1[i])-ord('0')) + carry
            newAns += chr(sum%10 + ord('0'))
            carry = sum//10
        # print(carry, newAns[::-1], 'trial2')
        if carry:
            newAns += chr(carry + ord('0'))
        # print(newAns, answer)   
        return newAns[::-1]+answer[::-1]