class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        oddIndex, evenIndex, index = 0, 0, 0
        
        while(index < len(A)):
            # print(index, A)
            if index%2 == 0 and A[index]%2 == 1:
                evenIndex = index+1
                while(A[evenIndex]%2 != 0):
                    evenIndex += 2
                A[index], A[evenIndex] = A[evenIndex], A[index]
                # index = evenIndex
            elif index%2 == 1 and A[index]%2 == 0:
                oddIndex = index+1
                while(A[oddIndex]%2 != 1):
                    oddIndex += 2
                A[index], A[oddIndex] = A[oddIndex], A[index]
                # index = oddIndex
            index += 1
            
        return A
            
        