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
