class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        numsSorted = nums
        numsSorted = sorted(numsSorted)
        for i in range(len(nums)):
            j = 0
            while (numsSorted[j] < nums[i]):
                j += 1
            answer.append(j)
        
        return answer
            
                