class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prod = [1]
        self.product = 1
        self.length = 1

    def add(self, num: int) -> None:
        self.nums.append(num)
        self.prod.append(self.product*num)
        self.product *= num
        # print(self.prod)
        self.length += 1
        

    def getProduct(self, k: int) -> int:
        if  k == 1:
            return int(self.nums[-1])
            
        # print(self.nums, k)
        if self.prod[self.length-k-1] > 0:
            # print(self.prod, self.prod[-1], self.prod[self.length-k-1])
            return int(self.prod[-1]/self.prod[self.length-k-1])
        else:
            product = 1
            length = len(self.nums)
            for j in range(k):
                # print('prod', product)
                product *= self.nums[length-j-1]
                if product == 0:
                    return 0
            return product
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)