class Solution:
    def reverse(self, x: int) -> int:
        if x >=0 :
            ans =  int(str(x)[::-1])
            if ans > (2**31) - 1:
                return 0
            return ans
        else:
            ans = -1*int(str(int(str(x)[::-1][:-1])))
            if ans < -1*(2**31):
                return 0
            return ans
        