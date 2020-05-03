class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        answer = ''
        
        while(A > 0 and B > 0):
            if A > B:
                answer += 'aab'
                A -= 2
                B -= 1
            elif B > A:
                answer += 'bba'
                A -= 1
                B -= 2
            else:
                answer += 'ab'*A
                A = 0
                B = 0
        
        answer += 'a'*A
        answer += 'b'*B
        
        return answer
                