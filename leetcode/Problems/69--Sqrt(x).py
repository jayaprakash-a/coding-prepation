class Solution:
    def mySqrt(self, x: int) -> int:
        answer = 0
        
        while(answer*answer <= x):
            answer += 1
        
        return answer-1
        