class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(list)
        columns = collections.defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    rows[i].append(board[i][j])
                    columns[j].append(board[i][j])
        values = []
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                entry = []
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l] != '.':
                            entry.append(board[k][l])
                values.append(entry)
        for entry in rows.values():
            if len(set(entry)) != len(entry):
                return False
        for entry in columns.values():
            if len(set(entry)) != len(entry):
                return False
        for entry in values:
            if len(set(entry)) != len(entry):
                return False
        
        return True