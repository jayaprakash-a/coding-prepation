class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        def expand(num):
            for index in range(len(num)):
                if num[index] == '(':
                    num = num[:index] + num[index+1:-1]*20
                    return float(num[:20])
            return float(num[:20])
        return expand(S) == expand(T)