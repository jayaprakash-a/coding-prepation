class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k > n//2 + 1:
            return -1
        for i in range(1, n+1):
            if n%i == 0:
                k -= 1
                if k == 0:
                    return i
        return -1
        