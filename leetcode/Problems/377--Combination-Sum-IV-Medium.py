class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        dp = collections.Counter()
        dp[0] = 1
        
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
                else:
                    break
        return dp[target]