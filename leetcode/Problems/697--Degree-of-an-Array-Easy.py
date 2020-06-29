class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        arr = {}
        vals = []
        for i in range(len(nums)):
            if nums[i] not in arr.keys():
                vals.append([1, i, i])
                arr[nums[i]] = len(vals) - 1
            else:
                vals[arr[nums[i]]][0] += 1
                vals[arr[nums[i]]][2] = i        
        def helper(x):
            return x[0], (x[1]-x[2])        
        vals = sorted(vals, key=helper, reverse=True)
        return vals[0][2] - vals[0][1] + 1
                
            