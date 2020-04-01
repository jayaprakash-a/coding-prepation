class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        answer = []
        prefix = 0
        for num in A:
            prefix = 2*prefix+num
            answer.append(prefix%5 == 0)
        
        return answer
            
        