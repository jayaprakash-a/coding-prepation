class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        loc, count = 0, 1
        for i in range(1, len(nums)):
            if nums[i] != nums[loc]:
                count = 1
                loc += 1
                nums[loc] = nums[i]
            else:
                count += 1
                if count <= 2:
                    loc += 1
                    nums[loc] = nums[i]
        # print(nums)
        for i in range(len(nums)-loc-1):
            nums.pop()
        
        return len(nums)
        