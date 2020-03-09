class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        answer = []
        dVal, iVal = len(S), 0
        
        for ch in S:
            if ch == 'I':
                answer.append(iVal)
                iVal += 1
            else:
                answer.append(dVal)
                dVal -= 1
        
        answer.append(dVal)
        
        return answer
                
        