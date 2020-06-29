class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        answer = 0
        i, j = 0, len(nums)-1
        for i in range(len(nums)):
            low, high = i, len(nums)-1
            val = i
            while low <= high:
                mid = (low+high)//2
                if nums[i] + nums[mid] <= target:
                    val = mid
                    low = mid+1
                else:
                    high = mid-1
            # print(i, val)
            if nums[i] + nums[val] <= target:
                answer += (1<<(val-i))
            else:
                break
        return answer%(10**9 + 7)
                