class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        happy, sumVal = 0, 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                happy += customers[i]
                customers[i] = sumVal
            else:
                sumVal += customers[i]
                customers[i] = sumVal
        customers.insert(0, 0)
        maxVal = 0
        for i in range(X, len(customers)):
            if customers[i] - customers[i-X] > maxVal:
                maxVal = customers[i] - customers[i-X]
        # pr
        return maxVal+happy
        # print(customers)
        