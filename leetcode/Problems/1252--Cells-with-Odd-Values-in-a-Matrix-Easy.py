class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # mat1 = [[0]*m]*n
        mat = []
        for i in range(n):
            mat.append([0]*m)
        # print(mat)
        # # mat[0][0] += 1
        # print(mat)
        for entry in indices:
            # print('entry', entry[0], entry[1])
            for i in range(m):
                mat[entry[0]][i] += 1
            # print('1st incre', mat)
            for i in range(n):
                mat[i][entry[1]] += 1
            # print('2nd incre', mat)
        count = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] %2 == 1:
                    count += 1
        return count
        
        