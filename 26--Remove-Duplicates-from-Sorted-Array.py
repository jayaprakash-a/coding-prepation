class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 0:
            return len(nums)
        val, index, position = nums[0], 1, 1
        while(index < len(nums)):
            # print('Debug1 ', index, val, nums[index])
            if val != nums[index]:
                # print('Debug2', position)
                nums[position] = nums[index]
                val = nums[index]
                position += 1

            index += 1
        return position
        