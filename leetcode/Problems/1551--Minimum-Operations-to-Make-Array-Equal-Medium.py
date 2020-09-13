class Solution:
    def minOperations(self, n: int) -> int:
        if n%2 == 1:
            mid = 2*(n//2) + 1
        else:
            mid = n
        
        answer = 0
        for i in range(n):
            answer += abs(mid-(2*i+1))
        
        return answer//2
        
        