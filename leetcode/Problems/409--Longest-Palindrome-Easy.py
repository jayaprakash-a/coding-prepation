class Solution:
    def longestPalindrome(self, s: str) -> int:
        charMap = {}
        
        for ch in s:
            if ch in charMap.keys():
                charMap[ch] += 1
            else:
                charMap[ch] = 1
        oddExists = False
        ans = 0
        for val in charMap.values():
            if val%2 == 0:
                ans += val
            else:
                oddExists = True
                ans += (val-1)
        
        if oddExists:
            return ans+1
        return ans