class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n==0:
            return 0
        low, high = 0, n-1
        while low <= high:
            mid = (low+high)//2
            if citations[mid] < n-mid:
                low = mid+1
            else:
                high = mid-1
        return n-low