class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 0, 1
        if n == 1:
            return second
        for i in range(n):
            temp = first
            first = second
            second = second + temp
        return second