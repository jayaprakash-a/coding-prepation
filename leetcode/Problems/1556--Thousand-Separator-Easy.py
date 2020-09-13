class Solution:
    def thousandSeparator(self, n: int) -> str:
        num = str(n)
        answer = ''
        count = 1
        for i in range(len(num)-1, -1, -1):
            answer = num[i] + answer
            if count%3 == 0 and i != 0:
                answer = '.' + answer
            count += 1
        
        return answer
        