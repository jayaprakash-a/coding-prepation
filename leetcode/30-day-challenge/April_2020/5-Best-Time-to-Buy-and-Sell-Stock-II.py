class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        profit = 0
        buyValue = prices[0]
        index = 1
        while(index < len(prices)):
            if prices[index] > buyValue:
                profit += (prices[index] - buyValue)
            buyValue = prices[index]
            index += 1
        
        return profit