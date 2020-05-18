class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, ch in enumerate(s):
            if ch not in s[i+1:] and ch not in s[:i]:
                return i
        return -1
        