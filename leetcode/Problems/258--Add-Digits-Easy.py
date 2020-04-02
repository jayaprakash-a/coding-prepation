class Solution:
    def addDigits(self, num: int) -> int:
        answer = 0
        for digit in str(num):
            answer = answer + int(digit)
        if answer and answer % 9:
            return answer % 9
        elif answer and answer % 9 == 0:
            return 9
        else:
            return 0
            
        