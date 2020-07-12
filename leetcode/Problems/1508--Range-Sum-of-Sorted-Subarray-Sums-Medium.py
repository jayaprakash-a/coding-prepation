class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sumVals = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sumVals.append(sum(nums[i:j+1]))
        sumVals = sorted(sumVals)
        # print(sumVals)
        # print(sumVals[left-1:right])
        return sum(sumVals[left-1:right])
            
        