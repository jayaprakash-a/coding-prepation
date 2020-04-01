class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        diagEntry = {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i+j) not in diagEntry.keys():
                    diagEntry[i+j] = [matrix[i][j]]
                else:
                    diagEntry[i+j] += [matrix[i][j]]
        
        diagSorted = sorted(diagEntry.keys())
        answer = []
        upDir = False
        for diag in diagSorted:
            if upDir:
                answer += diagEntry[diag]
                upDir = False
            else:
                answer += diagEntry[diag][::-1]
                upDir = True
        
        return answer
                
            
        