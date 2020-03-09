class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        for factor in [2,3,5]:
            
            while(num != 1 and num%factor == 0):
                num = num/factor
                # print(num)
            if num == 1:
                return True
        return False
        
        