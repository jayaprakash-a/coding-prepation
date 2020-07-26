class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low, high = matrix[0][0], matrix[-1][-1]
        answer = high
        while low <= high:
            mid = (low+high)//2
            val = 0
            for row in matrix:
                val += bisect.bisect_right(row, mid)
            if val >= k:
                answer = mid
                high = mid - 1
            else:
                low = mid +1
            
        return answer