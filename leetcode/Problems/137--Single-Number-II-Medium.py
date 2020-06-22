class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numsSet = collections.Counter(nums)
        
        for num in numsSet:
            if numsSet[num] == 1:
                return num
        