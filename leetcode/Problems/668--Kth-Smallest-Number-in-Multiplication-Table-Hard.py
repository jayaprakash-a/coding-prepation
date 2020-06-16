class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if k == m*n:
            return m*n
        low, high = 1, m*n
        def valid(mid):
            answer = 0
            for i in range(1, m+1):
                answer += min(mid//i, n)
            return answer >= k
        answer = -1
        while low < high:
            mid = (low+high)//2
            if valid(mid):
                high = mid
                answer = mid
            else:
                low = mid+1
        return answer