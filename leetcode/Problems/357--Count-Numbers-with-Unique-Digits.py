class Solution:
    def __init__(self):
        self.array = [1, 9, 9*9] 
        start = 8
        while(start > 0):
            lastVal = self.array[-1]
            self.array.append(lastVal*start)
            start -= 1
        sumVal = 0
        for i in range(len(self.array)):
            sumVal += self.array[i]
            self.array[i] = sumVal
            
    def countNumbersWithUniqueDigits(self, n: int) -> int:
       
        
        if n >= 10:
            return self.array[-1]
        return self.array[n]
        
        