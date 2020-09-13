class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew = ""
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                snew += ch
        return snew.lower() == snew.lower()[::-1]

        