class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        a1 = True
        for i in range(len(s1)):
            if s2[i] >= s1[i]:
                continue
            else:
                a1 = False
                break
        a2 = True
        for i in range(len(s1)):
            if s1[i] >= s2[i]:
                continue
            else:
                a2 = False
                break
        return a1 or a2