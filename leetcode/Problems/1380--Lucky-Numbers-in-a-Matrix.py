class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        count = []
        for i in range(len(matrix)):
            minRow = min(matrix[i])
            
            for j in range(len(matrix[i])):
                maxCol = max([matrix[k][j] for k in range(len(matrix))])
                if maxCol == minRow:
                    count.append(maxCol)
        return count
                
        