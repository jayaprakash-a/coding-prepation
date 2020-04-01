class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # print(bin(x^y))
        # print(x^y)
        return str(bin(x^y)).count('1')
        