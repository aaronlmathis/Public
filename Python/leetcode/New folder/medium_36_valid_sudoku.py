class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        # Check rows and columns
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                # Check row
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
                
                # Check column
                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
        
        # Check 3x3 sub-grids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = set()
                for k in range(3):
                    for l in range(3):
                        value = board[i+k][j+l]
                        if value != ".":
                            if value in subgrid:
                                return False
                            subgrid.add(value)
    
    return True
sol = Solution()
board =[[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
print(sol.isValidSudoku(board))
