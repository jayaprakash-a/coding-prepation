class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        matrix.insert(0, [0 for _ in range(n+1)])
        # matrix.append([0 for _ in range(n+2)])
        for i in range(1, m+1):
            matrix[i].insert(0, 0)
            # matrix[i].append(0)
        # print(matrix)
        answer = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                    answer += matrix[i][j]
        
        # print(matrix)
        
        return answer