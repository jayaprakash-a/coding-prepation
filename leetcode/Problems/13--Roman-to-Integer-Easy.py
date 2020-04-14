class Solution:
    def romanToInt(self, s: str) -> int:
        dic={ "I":1, "V":5,"X":10,"L":50, "C":100, "D":500, "M":1000, }

        li = [dic[j] for j in s]
        n = len(li)
        for i in range(1,n):
            if li[i] >li[i-1]:
                li[i-1] = - li[i-1]
        return sum(li)
        