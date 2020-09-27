class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        sumVals = {0: -1}
        for i in range(len(nums)):
            nums[i] = nums[i]%p
        totSum = sum(nums)%p
        if totSum == 0:
            return 0
        remSum = 0
        
        answer = len(nums)
        for i in range(len(nums)):
            remSum = (remSum+nums[i])%p
            val = totSum
            if (remSum-totSum)%p in sumVals:
                answer = min(answer, i-sumVals[(remSum-totSum)%p])
            sumVals[remSum] = i
        if answer == len(nums):
            return -1
        return answer

        