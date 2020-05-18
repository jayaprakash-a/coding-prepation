class Solution:
    def getVal(self, M, i, j):
        count, sumVal = 0, 0
        for l in range(i-1, i+2):
            for m in range(j-1, j+2):
                if l>=0 and l < len(M) and m>=0 and m<len(M[0]):
                    count += 1
                    sumVal += M[l][m]
        return sumVal//count
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        answer = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                answer[i][j] = self.getVal(M, i, j)
        return answer