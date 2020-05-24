class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        aInd, bInd = 0, 0
        answer = []
        while(aInd < len(A) and bInd < len(B)):
            start = max(A[aInd][0], B[bInd][0])
            end = min(A[aInd][1], B[bInd][1])
            
            if start <= end:
                answer.append([start, end])
            
            if A[aInd][1] <  B[bInd][1]:
                aInd += 1
            else:
                bInd += 1
        
        
        return answer