class Solution:
    def getPowerVals(self, n):
        answer = []
        upBound = math.ceil(math.sqrt(n))+1
        for j in range(2, upBound):
            answer.append(j*j)
        return answer
    def numSquares(self, n: int) -> int:
        arr = [0] + [i for i in range(1, n+1)]
        powVals = self.getPowerVals(n)
        for i in range(1, n+1):
            for jpow in powVals:
                if i < jpow:
                    break
                elif i >= jpow:
                    arr[i] = min(arr[i], arr[i-jpow]+1)
        
        return arr[-1]