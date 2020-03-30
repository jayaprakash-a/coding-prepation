class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # print(rangeMax)
        # if int(math.sqrt(c))**2 == c:
        #     return True
        rangeMax = math.ceil(math.sqrt(c/2))+1

        for i in range(0, rangeMax):
            # print(i**2, c-i**2)
            diff = c-i**2
            if diff >= 0:
                if int(math.sqrt(diff))**2 == diff:
                    # print(i, c)
                    return True
        return False
        