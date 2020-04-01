class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nStr = str(n)
        prodVal = 1
        sumVal = 0
        
        for ch in nStr:
            prodVal *= int(ch)
            sumVal += int(ch)
        
        return prodVal - sumVal
        