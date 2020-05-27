class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        answer = 0
        count = 0
        valFound = [-2]*(len(nums)+1)
        valFound[0] = -1
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if valFound[count] != -2:
            # if count in valFound.keys():
                if i - valFound[count] > answer:
                    answer = i - valFound[count]
            else:
                valFound[count] = i
                
        

        return answer
        