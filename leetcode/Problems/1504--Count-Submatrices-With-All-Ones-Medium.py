class Solution:
    def numSubmat(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        

        answer = 0
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0 and j != n-1:
                    matrix[i][j] = matrix[i][j+1] + 1
        
        # print(matrix)
        for j in range(n):
            i = m-1
            stack = [] 
            sumVal = 0
            while i >= 0: 
                c = 0
                while len(stack) != 0 and stack[-1][0] > matrix[i][j]: 
                    sumVal -= (stack[-1][1] + 1) * (stack[-1][0] - matrix[i][j]) 
                    c += stack[-1][1] + 1
                    stack.pop() 
                sumVal += matrix[i][j] 
                answer += sumVal 

                stack.append((matrix[i][j], c)) 
                i -= 1
        return answer