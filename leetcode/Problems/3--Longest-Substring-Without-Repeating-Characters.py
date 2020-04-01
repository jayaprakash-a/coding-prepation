class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maxValue, count = 0, 0
        charLoc = {}
        i = 0
        start = 0
        while(i < len(s)):
            # print(i, maxValue, count, charLoc)
            ch = s[i]
            if ch in charLoc.keys() and charLoc[ch] != -1:
                count = 0
                # print(ch)
                diff = i - start
                if diff > maxValue:
                    maxValue = diff
                i = charLoc[ch] + 1
                # print(ch, i)
                charLoc = {}
                start = i
            else:
                charLoc[ch] = i
                i += 1
                count += 1
        # print('answer', count)
        return max(maxValue, count)
            