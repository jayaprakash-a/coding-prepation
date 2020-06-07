class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subseq = {()}
        
        for num in nums:
            # print(subseq)
            subseq |= {sub + (num, ) for sub in subseq if len(sub) == 0 or sub[-1] <= num}
        
        # print(subseq)
        answer = [sub for sub in subseq if len(sub) >= 2]
        return answer