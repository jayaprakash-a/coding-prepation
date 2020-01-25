class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
#         28 ms  and 12.6 MB

        pos, index = 0, 0
        while(index < len(nums)):
            if nums[index] != val:
                nums[pos] = nums[index]
                pos += 1
            index += 1
        return pos
        
#         28 ms  and 12.7 MB
#         count = len(nums)
#         while val in nums:
#             nums.remove(val)
#         return len(nums)
          