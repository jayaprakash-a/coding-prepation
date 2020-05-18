class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num)-1] = -abs(nums[abs(num)-1])
        
        answer = []
        for i in range(len(nums)):
            if nums[i] > 0:
                answer.append(i+1)
        return answer