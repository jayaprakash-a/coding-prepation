class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # print(s.split())
        temp = s.split()
        if len(temp) == 0:
            return 0
        return len(temp[-1])
        