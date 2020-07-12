class Solution:
    def numSub(self, s: str) -> int:
        answer = 0
        value = 0
        for ch in s:
            if ch == '1':
                value += 1
                answer += value
            else:
                value = 0
        return answer%(10**9+7)