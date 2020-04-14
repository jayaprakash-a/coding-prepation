import math
class Solution:
    def calVal(self, arr, x):
        if x == 0:
            return float('inf')
        sumVal = 0
        for num in arr:
            sumVal += math.ceil(num/x)
        return sumVal
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        
        while( l <= r ):
            mid = l + (r-l)//2
            # print(mid)
            midSum = self.calVal(nums, mid)
            if midSum == threshold and self.calVal(nums, mid-1) > threshold:
                return mid
            if midSum > threshold:
                l = mid+1
            else:
                r = mid-1
                if self.calVal(nums, r)>threshold:
                    break
        return mid
        