class Solution:
    def trailingZeroes(self, n: int) -> int:
        five = 5
        count = 0
        while ( n // five != 0):
            count += (n // five)
            five *= 5
        return count
        