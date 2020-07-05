class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        val = x^y
        return bin(val).count('1')