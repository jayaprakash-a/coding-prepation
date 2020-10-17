class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r, c = len(rowSum), len(colSum)
        answer = [[0 for _ in range(c)] for _ in range(r)]
        total = 0
        for i in range(min(r, c)):
            minVal = min(rowSum[i], colSum[i])
            answer[i][i] += minVal
            rowSum[i] -= minVal
            colSum[i] -= minVal
        #     if rowSum[i] == 0:
        #         total += 1
        #     if colSum[i] == 0:
        #         total += 1
        # if total == r+c:
        #     return answer
        for i in range(r):
            if rowSum[i] != 0:
                for j in range(c):
                    minVal = min(rowSum[i], colSum[j])
                    answer[i][j] += minVal
                    rowSum[i] -= minVal
                    colSum[j] -= minVal                    
                    # if colSum[j] == 0:
                    #     total += 1
                    if rowSum[i] == 0:
                        # total += 1
                        break
        for i in range(c):
            if colSum[i] != 0:
                for j in range(r):
                    minVal = min(rowSum[j], colSum[i])
                    answer[i][j] += minVal
                    rowSum[j] -= minVal
                    colSum[i] -= minVal                    
                    # if colSum[i] == 0:
                    #     total += 1
                    if rowSum[j] == 0:
                        # total += 1
                        break               
        return answer
            