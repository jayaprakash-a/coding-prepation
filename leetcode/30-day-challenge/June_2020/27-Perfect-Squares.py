class Solution:
    def numSquares(self, n: int) -> int:

        squares = [i*i for i in range(1, math.ceil(math.sqrt(n)+1))]
        if squares[-1] == n:
            return 1
        def def_value(): 
            return sys.maxsize
      
        dp = {0:0}
        
        while n not in dp:
            newDp = defaultdict(def_value)
            for key in dp.keys():
                for entry in squares:
                    if key + entry <= n:
                        newDp[key+entry] = min(1+dp[key], newDp[key+entry])
            dp.update(newDp)
        return dp[n]