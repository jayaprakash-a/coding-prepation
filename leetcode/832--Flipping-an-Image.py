class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            row = A[i][::-1]
            for j in range(len(row)):
                row[j] = (row[j]+1)%2
            A[i] = row
        
        
        return A
            