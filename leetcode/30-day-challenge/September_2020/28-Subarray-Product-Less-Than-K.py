class Solution:
    def numSubarrayProductLessThanK(self, arr: List[int], k: int) -> int:
        if k <= 1:
            return 0
        answer = 0
        low, high, prod = 0, 0, 1
        while high < len(arr):
            prod *= arr[high]
            while prod >= k and high >= low:
                prod //= arr[low]
                low += 1
            answer += (high-low+1)
            high += 1
        return answer