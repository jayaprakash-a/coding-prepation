class Solution:
    def __init__(self):
        self.cache = {}
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            self.cache[n] = 1
            return self.cache[n]
        elif n == 1:
            self.cache[n] = x
            return self.cache[n]
        elif n == -1:
            self.cache[n] = 1/x
            return self.cache[n]
        elif n in self.cache.keys():
            return self.cache[n]
        if n % 2 == 0:
            
            self.cache[n//2] = self.myPow(x, n//2)
            return self.cache[n//2]**2
        else:
            
            if n > 0:
                self.cache[n//2] = self.myPow(x, n//2)
                # print(n//2, self.cache[n//2])
                return (self.cache[n//2]**2)*x
            else:
                self.cache[-(abs(n)//2)] = self.myPow(x, -(abs(n)//2))
                # print(n//2, self.cache[-(abs(n)//2)])
                return (self.cache[-(abs(n)//2)]**2)*(1/x)