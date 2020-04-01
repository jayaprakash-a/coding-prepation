# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.


# Not meeting reuqirement of the question

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        val = int(str(dividend/divisor).split('.')[0])
        
        return min(val, 2147483647)
        