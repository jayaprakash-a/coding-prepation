class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxIncl = []
        maxOverall = [0 for _ in range(len(nums))]
        if len(nums) <= 1:
            return len(nums)
        answer = 1
        i = 0
        nums.insert(0, nums[0]+limit+1)
        while i < len(nums)-1:
            j = i+1
            maxVal, maxInd, minVal, minInd = nums[i+1], i+1, nums[i+1], i+1
            while j < len(nums):
                if nums[j] > maxVal:
                    maxVal = nums[j]
                    maxInd = j
                if nums[j] < minVal:
                    minVal = nums[j]
                    minInd = j
                if maxVal - minVal <= limit:
                    # if i == 0:
                    answer = max(answer, j-i)
                    if answer == len(nums)-i:
                        return answer
                    # else:
                    #     answer = max(answer, j-i)
                else:
                    i = min(maxInd, minInd)-1
                    break
                
                j += 1
            i += 1
        return answer