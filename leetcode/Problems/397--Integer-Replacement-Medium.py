class Solution:
    def integerReplacement(self, n: int) -> int:
        if n&(n-1) == 0:
            return len(str(bin(n))) - 3
        if n%2 == 0:
            count = 0
            while(n%2 == 0):
                count += 1
                n = n//2
            return count+1+min(self.integerReplacement(n+1), self.integerReplacement(n-1))
        else:
            return 1+min(self.integerReplacement(n+1), self.integerReplacement(n-1))