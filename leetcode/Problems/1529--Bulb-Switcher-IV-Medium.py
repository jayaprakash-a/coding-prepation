class Solution:
    def minFlips(self, target: str) -> int:
        changes = 0
        prev = '0'
        for ch in target:
            if ch != prev:
                changes += 1
            prev = ch
        return changes