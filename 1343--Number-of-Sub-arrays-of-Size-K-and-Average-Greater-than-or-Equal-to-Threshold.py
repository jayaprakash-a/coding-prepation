class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        prefixSum = [0]
        sumVal, count = 0, 0
        for num in arr:
            sumVal += num
            prefixSum.append(sumVal)
            
        for i in range(len(prefixSum)-k):
            if prefixSum[i+k]-prefixSum[i] >= threshold*k:
                count += 1
        return count