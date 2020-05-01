class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        while True:
            temp = s
            for i in range(26):
                temp = temp.replace((chr(ord('a')+i)*k), '')
            if s == temp:
                return s
            s = temp