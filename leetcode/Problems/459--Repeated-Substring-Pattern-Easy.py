class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(1, length//2+1):
            # print(i, s[:i], len(s))
            if length % i == 0:
                # if s.replace(s[:i], '') == '':
                if s == (s[:i]*(length//i)):
                    return True
        return False