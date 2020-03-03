class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evenIndex, oddIndex = 0, len(A) - 1
        while(A[evenIndex] %2 == 0 and evenIndex < oddIndex):
            evenIndex += 1
        while(A[oddIndex] %2 == 1 and evenIndex < oddIndex):
            oddIndex -= 1
            
        while(evenIndex < oddIndex):
            A[evenIndex], A[oddIndex] = A[oddIndex],  A[evenIndex]
            while(A[evenIndex] %2 == 0 and evenIndex < oddIndex):
                evenIndex += 1
            while(A[oddIndex] %2 == 1 and evenIndex < oddIndex):
                oddIndex -= 1
                
        return A
            
            
        