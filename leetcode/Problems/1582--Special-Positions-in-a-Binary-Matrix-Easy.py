class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rowSum = [0 for _ in range(len(mat))]
        colSum = [0 for _ in range(len(mat[0]))]
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                rowSum[i] += mat[i][j]
                colSum[j] += mat[i][j]
        # print(rowSum, colSum)
        answer = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if rowSum[i] == colSum[j] == mat[i][j] == 1:
                    answer += 1
        return answer