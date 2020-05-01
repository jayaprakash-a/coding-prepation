class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return n&(n//2) == 0 and '0' not in str(bin(n|(n//2))).replace('0b', '')