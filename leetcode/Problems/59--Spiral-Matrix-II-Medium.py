class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]     
        mat[0][0], direction, nn, i, j, count = 1, 1, n*n, 0, 0, 0
        while(count < nn):
            # print(i, j, count+1, direction)
            mat[i][j] = count+1
            if direction == 1:
                if j < n-1 and mat[i][j+1] == 0:
                    j += 1
                else:
                    i, direction = i+1, 2
            elif direction == 2:
                if i < n-1 and mat[i+1][j] == 0:
                    i += 1
                else:
                    j, direction = j-1, 3
            elif direction == 3:
                if j >= 1 and mat[i][j-1] == 0:
                    j -= 1
                else:
                    i, direction = i-1, 4
            elif direction == 4:
                if i >= 1 and mat[i-1][j] == 0:
                    i -= 1
                else:
                    j, direction = j+1, 1
            count += 1
        return mat
            
        