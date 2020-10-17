class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        init = Counter()
        init[0] = 1
        for num in nums:
            temp = Counter()
            for entry in init:
                temp[entry - num] += init[entry]
                temp[entry + num] += init[entry]
            init = temp
        return init[S]