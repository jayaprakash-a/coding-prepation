class Solution:
    def maxSubarraySum(self, arr: List[int]) -> int:
        maxSumUptoI = 0
        maxSumIncludingI = 0
        left, right = 0, 0
        
        for i in range(len(arr)):
            maxSumUptoI = max(maxSumUptoI, maxSumIncludingI + arr[i], arr[i])                       
            maxSumIncludingI = max(maxSumIncludingI + arr[i], arr[i])
        
        return max(maxSumUptoI, 0)
    
    
    def maxProfit(self, prices: List[int]) -> int:
        priceChange = []
        for i in range(len(prices) - 1):
            priceChange.append(prices[i+1]-prices[i])

        return self.maxSubarraySum(priceChange)
            
    
            
        
    
        