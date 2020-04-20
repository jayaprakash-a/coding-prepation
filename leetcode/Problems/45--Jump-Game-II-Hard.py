class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 0
        answer = [length+1]*length
        answer[0] = 0
        
        
        for i in range(length):
            # print(num)
            if i > 0 and nums[i-1]-1 == nums[i]:
                continue
            for j in range(i+1, min(length, nums[i]+i+1)):
                # print(i, j)
                answer[j] = min(answer[i]+1, answer[j])
        return answer[-1]
        