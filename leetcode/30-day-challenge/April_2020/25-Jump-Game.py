class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        maxJump = 0
        for i in range(len(nums)):
            jump = nums[i]
            maxJump = max(jump, maxJump)
            if maxJump == 0 and i != len(nums)-1:
                return False
            maxJump -= 1
        return True