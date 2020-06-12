# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/discuss/477652/JavaC%2B%2BPython-1D-DP-O(1)-Space
class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(s, d):
            if s == ' ':
                return 0
            sord, dord = ord(s)-ord('A'), ord(d)-ord('A')
            sp = (sord//6, sord%6)
            dp = (dord//6, dord%6)
            # print(s, d, sp, dp)
            return abs(sp[0]-dp[0]) + abs(sp[1]-dp[1])
        dp, dp2 = {(' ', ' '): 0}, {}
        for ch in word:
            for (a, b) in dp:
                if (ch, b) not in dp2:
                    dp2[(ch, b)] = dp[(a, b)] + dist(a, ch)
                else:
                    dp2[(ch, b)] = min(dp2[(ch, b)], dp[(a, b)] + dist(a, ch))
                if (a, ch) not in dp2:
                    dp2[(a, ch)] = dp[(a, b)] + dist(b, ch)
                else:
                    dp2[(a, ch)] = min(dp2[(a, ch)], dp[(a, b)] + dist(b, ch))
            dp, dp2 = dp2, {}
            # print(dp)
        return min(dp.values())