import math

class Solution:
    def fact(self, n):
        if n <= 1:
            return 1
        return (n*self.fact(n-1))%(10**9+7)
    def countPrimes(self, n: int) -> int:
        if n <=1 :
            return 0
        if n == 2:
            return 1
        count = 0
        numList = [True]*(n)
        numList[0] = False
        numList[1] = True
        
        answer = n-2
        for i in range(2, math.ceil(math.sqrt(len(numList)))+1):
            if numList[i-1]:
                for j in range(2*i, len(numList)+1, i):
                    numList[j-1] = False

        return numList.count(True)
    def numPrimeArrangements(self, n: int) -> int:
        primeCount = self.countPrimes(n)
        
        return (self.fact(primeCount)*self.fact(n-primeCount))%(10**9+7)
        