class Solution:
    def generateTheString(self, n: int) -> str:
        chars = ['a', 'b', 'c']
        answer = ''
        if n == 1:
            return 'a'
        if n%2==0:
            answer += chars[0]*(n-1)
            answer += chars[1]
        else:
            answer += chars[0]*(n-2)
            answer += chars[1]
            answer += chars[2]
        
        return answer
            
            
        