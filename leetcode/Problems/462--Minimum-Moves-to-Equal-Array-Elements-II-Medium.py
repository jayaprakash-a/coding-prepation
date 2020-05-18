class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums = sorted(nums)
        vals = [nums[len(nums)//2-1], nums[len(nums)//2]]
        
        answer = float('inf')
        for val in vals:
            sumVal = 0
            for num in nums:
                sumVal += (abs(num-val))
            print(val, sumVal)
            answer = min(answer, sumVal)
        return answer