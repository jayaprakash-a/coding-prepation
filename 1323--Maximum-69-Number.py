class Solution:
    def maximum69Number (self, num: int) -> int:
        numDigit = list(str(num))
        for i in range(len(numDigit)):
            if numDigit[i] == '6':
                numDigit[i] = '9'
                break
        answer = ''.join(numDigit)
        return int(answer)
        