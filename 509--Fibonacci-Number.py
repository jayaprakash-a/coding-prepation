class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        
        curr, prev = 1, 0
        
        for i in range(N-1):
            temp = curr + prev
            prev = curr
            curr = temp
        
        return curr
        