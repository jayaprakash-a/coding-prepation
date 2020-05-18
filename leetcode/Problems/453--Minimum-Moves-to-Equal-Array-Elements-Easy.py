class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minVal, sumVal = min(nums), 0
        for num in nums:
            sumVal += (num-minVal)
        return sumVal