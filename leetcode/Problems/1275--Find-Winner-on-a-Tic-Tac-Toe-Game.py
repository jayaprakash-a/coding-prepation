class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        matrix = [[None, None, None], [None, None, None], [None, None, None]] 
        chance = 0
        for [x,y] in moves:
            if chance == 0:
                matrix[x][y] = 'X'
                chance = 1
            else:
                matrix[x][y] = 'O'
                chance = 0
        win1 = ['X', 'X', 'X']
        win2 = ['O', 'O', 'O']
        for i in range(3):
            if matrix[i] == win1:
                return 'A'
            elif matrix[i] == win2:
                return 'B'
        
        for i in range(3):
            col = [matrix[j][i] for j in range(3)]
            if col == win1:
                return 'A'
            elif col == win2:
                return 'B'
            
        diag1 = [matrix[0][0], matrix[1][1], matrix[2][2]]
        diag2 = [matrix[0][2], matrix[1][1], matrix[2][0]]
        
        if diag1 == win1 or diag2 == win1:
            return 'A'
        elif diag1 == win2 or diag2 == win2:
            return 'B'
        
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'
            
                