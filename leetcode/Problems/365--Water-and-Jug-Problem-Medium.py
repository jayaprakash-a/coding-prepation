# https://www.math.tamu.edu/~dallen/hollywood/diehard/diehard.htm
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x+y < z:
            return False
        if x+y == z or y == z or x == z:
            return True
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        return z % gcd(max(x, y), min(x, y)) == 0