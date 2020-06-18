class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return 
        R, C = len(board), len(board[0])
        
        queue = collections.deque()
        for i in range(R):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][C-1] == 'O':
                queue.append((i, C-1))
        for i in range(C):
            if board[0][i] == 'O':
                queue.append((0, i))
            if board[R-1][i] == 'O':
                queue.append((R-1, i))
        while queue:
            i, j = queue.popleft()
            board[i][j] = 'N'
            if 0<=i-1<R and 0<=j<C and board[i-1][j] == 'O':
                queue.append((i-1, j))
            if 0<=i+1<R and 0<=j<C and board[i+1][j] == 'O':
                queue.append((i+1, j))
            if 0<=i<R and 0<=j-1<C and board[i][j-1] == 'O':
                queue.append((i, j-1))
            if 0<=i<R and 0<=j+1<C and board[i][j+1] == 'O':
                queue.append((i, j+1))
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        