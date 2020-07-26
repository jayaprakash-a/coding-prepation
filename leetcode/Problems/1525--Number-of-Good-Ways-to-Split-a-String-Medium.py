class Solution:
    def numSplits(self, s: str) -> int:
        # print('----------')
        c = Counter('')
        d = Counter(s)
        dCount = len(d)
        answer = 0
        for ch in s:
            c[ch] += 1
            d[ch] -= 1
            if d[ch] == 0:
                dCount -= 1
            # print(len(c), dCount)
            if len(c) == dCount:
                answer += 1
        return answer
            