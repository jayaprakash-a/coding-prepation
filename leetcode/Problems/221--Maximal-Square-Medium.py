
class Solution:
    def printMat(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(mat[i][j], end = ' ')
            print()
        print('------')
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        # self.printMat(matrix) 
        newMat = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
        maxVal = 0
        for i in range(1, len(newMat)):
            for j in range(1, len(newMat[0])):
                if matrix[i-1][j-1] == '1':
                    newMat[i][j] = min(newMat[i-1][j], newMat[i][j-1], newMat[i-1][j-1]) + 1
                    maxVal = max(maxVal, newMat[i][j])
        # self.printMat(newMat) 
        return maxVal**2