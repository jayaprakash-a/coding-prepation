class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return math.floor(math.sqrt(num))**2 == num