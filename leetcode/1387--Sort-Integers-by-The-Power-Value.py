import math
class Solution:

      
    def compare(self, x):
        return x[1], x[0]
    def getKth(self, lo: int, hi: int, k: int) -> int:
        val = []
        for num in range(lo, hi+1):
            number = num
            count = 0
            while(int(num&(num-1)) != 0):
                if num%2 == 0:
                    num = num//2
                else:
                    num = 3 * num + 1
                count += 1
            count += int(math.log(num, 2))
            val.append([number, count])
        # print(val)
        valSort = sorted(val, key=self.compare)
        return valSort[k-1][0]
        # return self.kthSmallest(val, 0, len(val) - 1, k)
            
            
        