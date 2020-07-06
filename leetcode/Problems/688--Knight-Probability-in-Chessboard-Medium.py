class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        ans = [[[0.0 for _ in range(N)] for _ in range(N)] for _ in range(K+1)]
        move = [[-2,-1],[-1,-2],[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1]]
        def validMoves(K, N, r, c):
            if r < 0 or r > N - 1 or c < 0 or c > N - 1:
                return 0
            if K == 0:
                return 1
            if ans[K][r][c] != 0.0:
                return ans[K][r][c]
            value = 0.0
            for i in range(8):
                value += (0.125 * validMoves(K-1, N, r + move[i][0], c+move[i][1]))
            ans[K][r][c] = value
            return value
        return validMoves(K, N, r, c)
            