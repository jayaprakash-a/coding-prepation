class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxVal = nums[0]
        minVal = nums[0]
        answer = nums[0]
        for num in nums[1:]:
            prevMax, prevMin = maxVal, minVal
            if num > 0:
                maxVal = max(num, num*prevMax)
                minVal = min(num, num*prevMin)
            else:
                maxVal = max(num, num*prevMin)
                minVal = min(num, num*prevMax)
            answer = max(answer, maxVal)
            # print(maxVal, minVal, answer)
        return answer
        