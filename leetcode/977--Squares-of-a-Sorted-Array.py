class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        negInd, posInd = 0, 0
        
        while(negInd < len(A) and A[negInd] < 0 ):
            negInd += 1
            # print(negInd)
        posInd = negInd
        negInd -= 1
        
        answer = []
        while(posInd < len(A) and negInd >= 0):
            if A[posInd] <= abs(A[negInd]):
                answer.append(A[posInd]**2)
                posInd += 1
            else:
                answer.append(A[negInd]**2)
                negInd -= 1
        
        while(posInd < len(A) and posInd >= 0):
            answer.append(A[posInd]**2)
            posInd += 1
        
        while(negInd >= 0 and negInd < len(A)):
            answer.append(A[negInd]**2)
            negInd -= 1
        
        return answer
              
                
                
            
        