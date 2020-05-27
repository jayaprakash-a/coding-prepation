class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        maxValue = max(piles)
        l, r = 1, maxValue
        answer = maxValue
        while(l < r):
            mid = (r+l)//2
            value = 0
            for num in piles:
                value += math.ceil(num/mid)
            if value <= H:
                answer = mid
                r = mid
            else:
                l = mid + 1
        return answer
                