class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        sumval = sum(nums)
        nums = sorted(nums, reverse=True)
        answer = []
        newSum = 0
        for i in range(len(nums)):
            answer.append(nums[i])
            newSum += nums[i]
            sumval -= nums[i]
            if newSum > sumval:
                break
        return answer
