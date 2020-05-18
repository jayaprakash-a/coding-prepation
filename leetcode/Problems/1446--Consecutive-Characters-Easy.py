class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLen = 1
        maxVal = 1
        prev = s[0]
        for ch in s[1:]:
            if ch == prev:
                maxVal += 1
                maxLen = max(maxLen, maxVal)
            else:
                prev = ch
                maxVal = 1
                maxLen = max(maxLen, maxVal)
        return maxLen