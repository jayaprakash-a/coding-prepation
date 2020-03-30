# Both are workign solutions.
# One is sequential another by formulae 

class Solution:
    def getVal(self, n, k):
        p1, p2 = 1, 1
        for i in range(1, k+1):
            p1 *= i
            p2 *= (n-i-1)
        return p2//p1
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        answer = []
        rowIndex += 2
        for i in range(1, rowIndex//2):
            # print('for', i)
            answer.append(self.getVal(rowIndex, i))
        if rowIndex %2 == 1:
            answer = answer + answer[::-1] + [1]
        else:
            answer = answer + answer[:-1][::-1] + [1]
        answer.insert(0 ,1)
        return answer
#     def getRow(self, rowIndex: int) -> List[int]:

#         if rowIndex == 0:
#             return [1]
#         if rowIndex == 1:
#             return [1,1]
#         answer = [[1], [1,1]]
        
#         newArr = []
#         for i in range(rowIndex - 1):
#             newArr = []
#             for j in range(len(answer[-1]) - 1):
#                 newArr.append(answer[-1][j+1] + answer[-1][j])
#             newArr.append(1)
#             newArr.insert(0, 1)
            
#             answer.append(newArr)
        
#         return newArr