class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num = 1
        while(True):
            if num == n:
                return True
            elif num > n:
                return False
            num *= 3
        