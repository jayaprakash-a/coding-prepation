class Solution:
    def longestPrefix(self, s: str) -> str:
        answer = 0
        for i in range(len(s)):
            # print(s[:i], s[-i:], i)
            if s[:i] == s[-i:]:
                answer = i
        return s[:answer]
                
        