class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        answer = [[1], [1,1]]
        
        for i in range(numRows - 2):
            newArr = []
            for j in range(len(answer[-1]) - 1):
                newArr.append(answer[-1][j+1] + answer[-1][j])
            newArr.append(1)
            newArr.insert(0, 1)
            
            answer.append(newArr)
        
        return answer
        