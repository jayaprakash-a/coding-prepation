class StockSpanner:

    def __init__(self):
        
        self.prices = []
        self.recent = []
    
    def next(self, price: int) -> int:
        
        if len(self.prices) == 0:
            self.recent.append(len(self.prices))
            self.prices.append(price)
            return 1
        
        count, index = 0, -1
        
        while len(self.recent) > 0 and price >= self.prices[self.recent[-1]]:
            self.recent.pop()
        
        if len(self.recent) == 0:
            count = len(self.prices) + 1
        else:
            count = len(self.prices) - self.recent[-1]

        self.recent.append(len(self.prices))
        self.prices.append(price)
        
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)