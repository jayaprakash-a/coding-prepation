class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and int(log(num, 4)) == log(num, 4)