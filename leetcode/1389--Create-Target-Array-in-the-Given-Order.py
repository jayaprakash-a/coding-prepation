class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        answer = []
        for i in range(len(index)):
            answer.insert(index[i], nums[i])
        
        return answer
            
        