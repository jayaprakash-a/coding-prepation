class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0,1,1]
        if n <= 2:
            return ans[n]
        for i in range(n-2):
            val = ans[i]+ans[i+1]+ans[i+2]
            ans.append(val)
        
        return ans[-1]
        