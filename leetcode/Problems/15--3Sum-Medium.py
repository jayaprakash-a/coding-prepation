class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                return answer
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            
            while(left < right):
                sumVal = nums[i] + nums[left] + nums[right]
                if sumVal < 0:
                    left += 1
                elif sumVal > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    while(left < right and nums[left] == nums[left+1]):
                        left += 1
                    while(left < right and nums[right] == nums[right-1]):
                        right -= 1
                    left += 1
                    right -= 1
        return answer