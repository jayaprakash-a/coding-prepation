class Solution:
    def getEntry(self, x, y, matrix, dir):
        if dir == 0:
            return matrix[x][y:len(matrix[0])-y], x, len(matrix[0])-y-1
        elif dir == 1:
            return [matrix[x+i][y] for i in range(1, len(matrix)-2*x) ], len(matrix)-x-1, y
        elif dir == 2:
            return matrix[x][len(matrix[0])-y-1:y][::-1], x, len(matrix[0])-y-1
        elif dir == 3:
            return [matrix[i][y] for i in range(len(matrix)-x, x) ][::-1], len(matrix)-x, y+1
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        i, j = 0, 0
        count = 0
        if len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        direction = 0
        while(count < m*n):
            res, i, j = self.getEntry(i, j, matrix, direction)
            direction = (direction+1)%4
            count += len(res)
            answer += res
            # print(answer)
        return answer