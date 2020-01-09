class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).replace('0b', '').count('1')
        