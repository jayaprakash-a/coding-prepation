import math
class Solution:
    def isPalindrome(self, N):
        return str(N) == str(N)[::-1]
    def isPrime(self, N):
        if N == 2:
            return True
        for i in range(2, math.ceil(math.sqrt(N) + 1)):
            if N%i == 0:
                return False
        return True
    def primePalindrome(self, N: int) -> int:
        N = max(2, N)
        while(True):
            
            if self.isPalindrome(N):
                if self.isPrime(N):
                    return N
            if 10000000 < N and N < 100000000:
                N = 100000001
                continue
            if N%2 == 0:
                N += 1
            else:
                N += 2
                
        
        