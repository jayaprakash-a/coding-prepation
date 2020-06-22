import sys
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n, m = len(dungeon), len(dungeon[0])
        answer = [[sys.maxsize for _ in range(m+1)] for _ in range(n+1)]
        answer[-2][-1] = 1
        answer[-1][-2] = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                answer[i][j] = min(answer[i+1][j], answer[i][j+1]) - dungeon[i][j]
                if answer[i][j] <= 0:
                    answer[i][j] = 1
        return answer[0][0]