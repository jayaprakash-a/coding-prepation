class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        startPos, index, endPos = 0, 0, len(nums) - 1
        while(index < len(nums)):
            if nums[index] != 0:
                nums[startPos] = nums[index]
                startPos += 1
            # else:
            #     nums[endPos] = 0
            #     endPos -= 1
            index += 1
        while(startPos < len(nums)):
            nums[startPos] = 0
            startPos += 1
        # return pos