class Solution:
    def countBits(self, num: int) -> List[int]:
        answer = [0]*(num+1)
        
        for i in range(1, num+1):
            answer[i] = (i%2)+answer[i//2]
        
        return answer