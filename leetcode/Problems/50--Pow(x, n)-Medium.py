class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n == 1):
            return x
        elif (n == 0):
            return 1.0
        elif n== -1:
            return 1/x
        
        if x == 0:
            return 0.0
        if x == 1:
            return 1.0
        
        
        if n > 0:
            if n%2 == 0:
                return self.myPow(x, n//2) ** 2
            else:
                return self.myPow(x, n//2) ** 2 * x
        else:
            if n%2 == 0:
                # print('here')
                return self.myPow(x, n//2) ** 2
            else:
                # print(n, n//2)
                return self.myPow(x, n//2) ** 2 * x