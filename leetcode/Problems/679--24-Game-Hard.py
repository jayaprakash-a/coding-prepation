import itertools
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            # print(nums[0])
            return abs(nums[0]-24) < 1e-5
        elif len(nums) == 4:
            for [a, b, c, d] in itertools.permutations(nums):
                a3 = False
                a1 = self.judgePoint24([a+b, c, d])
                a2 = self.judgePoint24([a*b, c, d])
                if b != 0:
                    a3 = self.judgePoint24([a/b, c, d])
                a4 = self.judgePoint24([a-b, c, d])
                if a1 or a2 or a3 or a4:
                    return True
            return False
        elif len(nums) == 3:
            for [a, b, c] in itertools.permutations(nums):
                a3 = False
                a1 = self.judgePoint24([a+b, c])
                a2 = self.judgePoint24([a*b, c])
                if b != 0:
                    a3 = self.judgePoint24([a/b, c])
                a4 = self.judgePoint24([a-b, c])
                if a1 or a2 or a3 or a4:
                    return True
            return False
        elif len(nums) == 2:
            for [a, b] in itertools.permutations(nums):
                a3 = False
                a1 = self.judgePoint24([a+b])
                a2 = self.judgePoint24([a*b])
                if b != 0:
                    a3 = self.judgePoint24([a/b])
                a4 = self.judgePoint24([a-b])
                if a1 or a2 or a3 or a4:
                    return True
            return False
