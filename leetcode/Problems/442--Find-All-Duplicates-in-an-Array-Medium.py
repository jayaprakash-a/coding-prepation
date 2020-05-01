class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)+1
        for i in range(len(nums)):
            num = nums[i]
            if num >= n*n:
                num = num//(n*n)
            elif num >= n:
                num = num//n
            nums[num-1] *= n
            
        answer = []
        for i in range(len(nums)):
            if nums[i] >= n*n:
                answer.append(i+1)
        return answer
            
        