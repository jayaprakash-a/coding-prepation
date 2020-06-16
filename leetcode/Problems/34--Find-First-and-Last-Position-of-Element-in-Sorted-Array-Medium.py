class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [-1, -1]
        l, r, val = 0, len(nums)-1, -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
                val = mid
        answer[0] = val
        l, r, val = 0, len(nums)-1, -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                l = mid+1
                val = mid
        answer[1] = val
        
        return answer