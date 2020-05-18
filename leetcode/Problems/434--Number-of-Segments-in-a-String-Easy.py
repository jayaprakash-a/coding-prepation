class Solution:
    def countSegments(self, s: str) -> int:
        return sum([1 for ch in s.split(' ') if ch != ''])