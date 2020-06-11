class Solution:
    def convertToBase7(self, num: int) -> str:
        def getRep(num):
            answer = ''
            while(num):
                answer += str(num%7)
                num //= 7
            return answer[::-1]
        answer = getRep(abs(num))
        if num > 0:
            return answer
        elif num == 0:
            return '0'
        else:
            return '-' + answer