class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxInc = nums[0]
        maxOverall = nums[0]
        for i in range(1, len(nums)):
            maxInc = max(nums[i], nums[i]+maxInc)
            maxOverall = max(maxOverall, maxInc)
        return max(maxOverall, 0)%(10**9+7)
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if len(arr) == 0:
            return 0
        modVal = 10**9+7
        if len(arr) == 1 and arr[0] >= 0:
            return (k*arr[0])%modVal
        elif len(arr) == 0 and arr[0] < 0:
            return 0
        if sum(arr) < 0 or k == 2:
            return self.maxSubArray(arr+arr)
        elif k == 1:
            return self.maxSubArray(arr)
        
        maxPre = float('-inf')
        sumVal = 0
        for num in arr:
            sumVal += num
            maxPre = max(maxPre, sumVal)
        
        maxSuff = float('-inf')
        sumVal = 0        
        for num in arr[::-1]:
            sumVal += num
            maxSuff = max(maxSuff, sumVal)
        # print(maxSuff, maxPre, sum(arr))
        return (maxSuff+(k-2)*sum(arr)+maxPre)%modVal
        