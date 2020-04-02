class Solution:
    def addNumbers(self, num1, num2):
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
    def multiplySingleDigit(self, num, digit):
        answer = ''
        carry = 0
        for ch in num[::-1]:
            prod = (ord(ch)-ord('0')) * (ord(digit)-ord('0')) + carry
            answer += chr(prod%10 + ord('0'))
            carry = prod//10
        if not carry:
            return answer[::-1]
        else:
            answer += chr(carry + ord('0'))
            return answer[::-1]
    def multiply(self, num1: str, num2: str) -> str:
        # return str(int(num1)*int(num2))

        
        prodVals = {}
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        answer = '0'
        for i in range(len(num2)-1, -1, -1):
            if num2[i] == 1:
                prodVal = num1
            elif num2[i] == 0:
                prodVal = '0'
            elif num2[i] not in prodVals.keys():
                prodVal = self.multiplySingleDigit(num1, num2[i])
                prodVals[num2[i]] = prodVal
            else:
                prodVal = prodVals[num2[i]]
            prodVal += ('0'*(len(num2)-1-i))
            answer = self.addNumbers(answer, prodVal)
        
        return answer
        
        