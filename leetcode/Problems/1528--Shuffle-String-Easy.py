class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        charArr = ['' for _ in range(len(s))]
        for i in range(len(s)):
            charArr[indices[i]] = s[i]
        return ''.join(charArr)