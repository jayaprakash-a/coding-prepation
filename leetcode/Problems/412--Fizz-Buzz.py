class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 0:
            return []
        answer = []
        for i in range(1, n+1):
            val = ''
            if i%3==0:
                val += 'Fizz'
            if i%5==0:
                val += 'Buzz'
            
            if val =='':
                answer.append(str(i))
            else:
                answer.append(val)
        
        return answer
            
        