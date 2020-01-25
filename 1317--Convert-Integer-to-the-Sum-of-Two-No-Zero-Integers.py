class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        strNum = str(n)
        for digitPos in range(len(strNum)):
            if strNum[digitPos] == '0':
                break
            answer = 0
        if digitPos < len(strNum) - 1 or (digitPos == len(strNum) - 1 and strNum[-1] == '0'):
            val = strNum[digitPos:]
            answer = int(val) + 1
        elif (digitPos == len(strNum) - 1 and strNum[-1] == '1'):
            revStr = strNum[::-1]
            for digitPos in range(len(strNum)):
                if revStr[digitPos] != '1':
                    break
            val = '1'*digitPos
            answer = int(val) + 1
        else:
            answer = 1
            
        if '0' not in str(answer) and '0' not in str(n-answer):
            
            return [answer, n - answer]
        for i in range(1, n):
            if '0' not in str(i) and '0' not in str(n-i):
                return [i, n-i]
            
        