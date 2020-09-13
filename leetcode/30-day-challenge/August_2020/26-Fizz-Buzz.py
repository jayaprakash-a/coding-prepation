class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            val = ''
            if i%3 == 0:
                val += 'Fizz'
            if i%5 == 0:
                val += 'Buzz'
            if val == '':
                answer.append(str(i))
            else:
                answer.append(val)
        return answer