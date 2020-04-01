class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        midIndex = len(nums)//2
        print(nums, midIndex)
        if nums[midIndex] == target:
            return midIndex
        elif target > nums[midIndex]:
            # print('result', nums[(midIndex+1):])
            # result = self.search(nums[(midIndex+1):], target)
            # print('result', nums, result)
            # if result != -1:
                # return midIndex + result + 1
            
            # print('res1', nums[(midIndex+1):])
            res1 = self.search(nums[(midIndex+1):], target)
            # print('res1', nums, res1)
            # print('res2', nums[:(midIndex-1)])
            res2 = self.search(nums[:(midIndex)], target)
            # print('res2', nums, res2)
            if res1 != -1:
                return midIndex + res1 + 1
            if res2 != -1:
                return res2
        else:
            # print('res1', nums[(midIndex+1):])
            res1 = self.search(nums[(midIndex+1):], target)
            # print('res1', nums, res1)
            # print('res2', nums[:(midIndex-1)])
            res2 = self.search(nums[:(midIndex)], target)
            # print('res2', nums, res2)
            if res1 != -1:
                return midIndex + res1 + 1
            if res2 != -1:
                return res2
            
        return -1
        
            
        