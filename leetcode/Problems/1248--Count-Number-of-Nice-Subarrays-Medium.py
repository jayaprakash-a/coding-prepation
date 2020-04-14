class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        answer = 0
        count = 0
        valFound = [0]*(len(nums)+1)
        valFound[0] = 1
        for i in range(len(nums)):
            if nums[i]%2 == 1:
                count += 1
            valFound[count] += 1
            if count - k >= 0:
                answer += valFound[count-k]
        

        return answer