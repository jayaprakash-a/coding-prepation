class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while(left <= right):
            midIndex = (left+right)//2
            if nums[midIndex] == target:
                return midIndex
            elif nums[midIndex] > target:
                right = midIndex-1
            else:
                left = midIndex+1
        return -1
