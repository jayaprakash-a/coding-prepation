import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sumVal = 0
        for num in nums:
            val = num + 1
            count = 2
            # print(int(math.sqrt(num))**2)
            if int(math.sqrt(num))**2 == num:
                continue
            for i in range(2, math.ceil(math.sqrt(num))):
                if num%i == 0:
                    # print(num, i)
                    val += i
                    val += (num//i)
                    count += 2
                    if count > 4:
                        break
            if count == 4:
                sumVal += val
        
        return sumVal
            
        