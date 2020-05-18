class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        isIncrease = True
        
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                return False
            if A[i] > A[i+1] and  i == 0:
                return False
            elif A[i] > A[i+1] and isIncrease:
                isIncrease = False
            elif not isIncrease and A[i] < A[i+1]:
                return False
        
        return True and not isIncrease