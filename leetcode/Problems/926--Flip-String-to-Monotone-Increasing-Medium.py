class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        answer, oneCount = 0, 0
        for ch in S:
            if ch == '0' and oneCount == 0:
                continue
            elif ch == '0':
                answer += 1
            else:
                oneCount += 1
            answer = min(answer, oneCount)
        return answer