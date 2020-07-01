class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 1
        answer = 0
        while n >= start:
            answer += 1
            n -= start
            start += 1
        return answer