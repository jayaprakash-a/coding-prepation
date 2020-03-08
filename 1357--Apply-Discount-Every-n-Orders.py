class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        # self.products = products
        # self.prices = prices
        self.price = {}
        self.count = 0
        for i in range(len(products)):
            self.price[products[i]] = prices[i]
            

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        cost = 0.0
        # if self.count % self.n == 0:
        for i in range(len(product)):
            cost += amount[i]*self.price[product[i]]
        
        if self.count % self.n == 0:
            cost = (cost - (self.discount * cost) / 100)
        
        return cost
            
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)