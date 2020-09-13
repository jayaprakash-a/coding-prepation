class Solution:
    def minDays(self, n: int) -> int:
        self.cache = {0: 0, 1: 1}
        def helper(n):
            # print(n, n%2, n%3)
            if n in self.cache:
                return self.cache[n]
            # print(n%2 + helper(n//2), n%3 + helper(n//3))
            answer = 1 + min(n%2 + helper(n//2), n%3 + helper(n//3))
            self.cache[n] = answer
            return answer
        return helper(n)