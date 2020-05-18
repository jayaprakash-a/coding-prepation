class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        start = 0
        end = sum(nums)
        for i in range(len(nums)):
            
            end -= nums[i]
            # print(start, end)
            if start == end:
                return i
            start += nums[i]
        return -1