class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for ch in S:
            if ch in J:
                count += 1
        return count
        