class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        def countSort(arr, base, multiplier):
            tempArr = [0  for _ in range(len(arr))]
            count = [0 for _ in range(multiplier)] # To store the count of digit at `base' position of number
            for num in arr:
                count[(num//base)%multiplier] += 1
            for i in range(1, multiplier):
                count[i] += count[i-1] # Cumulative sum
            for i in range(len(arr)-1, -1, -1):
                tempArr[count[(arr[i]//base)%multiplier] - 1] = arr[i] # get new location of number based on cumulative sum
                count[(arr[i]//base)%multiplier] -= 1
            for i in range(len(arr)):
                arr[i] = tempArr[i]
            return arr
        def radixSort(arr):
            maxVal = max(arr)
            base, multiplier = 1, 10
            while maxVal//base:
                arr = countSort(arr, base, multiplier)
                base *= multiplier
            return arr
        nums = radixSort(nums)
        answer = -1
        for i in range(len(nums)-1):
            answer = max(answer, nums[i+1]-nums[i])
        
        return answer