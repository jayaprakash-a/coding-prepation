class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)
        answer = -1
        low, high = 0, nums[-1]
        while low <= high:
            mid = (low+high)//2
            index = bisect.bisect_left(nums, mid)
            # print(mid, index, len(nums)-index)
            if len(nums) - index == mid:
                answer = mid
                high = mid - 1
            elif len(nums) - index > mid:
                low = mid+1
            else:
                high = mid-1
        # print('------')
        return answer