class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heightsUnsorted = heights
        heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != heightsUnsorted[i]:
                count += 1
        return count
        