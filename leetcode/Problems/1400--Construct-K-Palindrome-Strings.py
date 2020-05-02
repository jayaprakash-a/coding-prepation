class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        charCount = {}
        for ch in s:
            if ch not in charCount.keys():
                charCount[ch] = 1
            else:
                charCount[ch] += 1
        odd, ans = 0, 0
        for key in charCount.keys():
            if charCount[key] % 2 == 0:
                ans += charCount[key]//2
            else:
                ans += charCount[key]//2
                odd += 1
                if odd > k:
                    return False
        if ans+odd >= k or odd+2*ans >= k:
            return True
        return False
