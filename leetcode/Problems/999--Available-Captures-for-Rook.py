class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        count = 0
        l, r, found = 0, 0, False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    l, r = i, j
                    found = True
                    break
            if found:
                break
        a, b = l-1, r
        while(a >= 0 and (board[a][b] != 'p' and board[a][b] != 'B')):
            a -= 1

        if b >= 0 and board[a][b] == 'p':
            count += 1

        a, b = l, r-1
        while(b >= 0 and (board[a][b] != 'p' and board[a][b] != 'B')):
            b -= 1

        if b >= 0 and board[a][b] == 'p':
            count += 1

        a, b = l+1, r
        while(a < 8 and (board[a][b] != 'p' and board[a][b] != 'B')):
            a += 1

        if a < 8 and board[a][b] == 'p':
            count += 1

        a, b = l, r+1
        while(b < 8 and (board[a][b] != 'p' and board[a][b] != 'B')):
            b += 1

        if b < 8 and board[a][b] == 'p':
            count += 1

        return count
