class Solution:
    def __init__(self):
        self.result = set()
    def genPerm(self, nums, pos):
        if pos == len(nums):
            self.result.add(tuple(nums))
            return
        for i in range(pos, len(nums)):
            nums[i], nums[pos] = nums[pos], nums[i]
            self.genPerm(nums, pos+1)
            nums[i], nums[pos] = nums[pos], nums[i]
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.genPerm(nums, 0)
        answer = []
        for entry in self.result:
            answer.append(list(entry))
        return answer
        