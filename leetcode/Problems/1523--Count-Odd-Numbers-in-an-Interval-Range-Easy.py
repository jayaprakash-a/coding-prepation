class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            return low%2 
        if low %2 == 0:
            low += 1
        if high%2 == 0:
            high -= 1
        if high < low:
            return 0
        return (high-low)//2 + 1