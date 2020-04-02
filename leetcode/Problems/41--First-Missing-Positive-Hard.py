class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        start = 1
        while True:
            if start in nums:
                 start +=1
            else:
                return start


















                