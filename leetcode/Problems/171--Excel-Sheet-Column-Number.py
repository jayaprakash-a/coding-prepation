class Solution:
    def titleToNumber(self, s: str) -> int:
        val = 0
        # length = 0
        num = 1
        length = 1
        for ch in s[::-1]:
            print(ord(ch) - ord('A') + 1, end = " ")
            val = val + num*(ord(ch) - ord('A') + 1)
            num = 26**length
            length += 1
        return val
            
        