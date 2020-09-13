class Solution:
    def longestPalindrome(self, s: str) -> int:
        charMap = Counter(s)
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