class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        minDist = 0
        answer = float('inf')
        for i in range(len(nums)-2):

            left, right = i+1, len(nums)-1
            
            while(left < right):
                sumVal = nums[i] + nums[left] + nums[right]
                if sumVal < target:
                    if abs(target-sumVal) < answer:
                        # print(nums[i], nums[left], nums[right])
                        minDist = nums[i] + nums[left] + nums[right]
                        answer = abs(target-sumVal)
                    left += 1
                elif sumVal > target:
                    if abs(target-sumVal) < answer:
                        # print(nums[i], nums[left], nums[right])
                        minDist = nums[i] + nums[left] + nums[right]
                        answer = abs(target-sumVal)
                    right -= 1
                else:
                    return target

        return minDist