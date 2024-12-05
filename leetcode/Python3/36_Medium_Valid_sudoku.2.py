"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Declare rows, cols, subgrids lists to hold sets that track numbers in each row, col, subgrid
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]

        # Iterate through every space of the board.
        #   - Set num to board[r][c]
        #   - Determine the subgrid (k) using formula (row // 3) * 3 + (col // 3)
        #   - Ignore empty spaces
        #   - For non-empty spaces, check to see if num is part of the cell for that row, col, or subgrid.
        #   - If not, add them to the set for each row, col, subgrid (rows[r], subgrids[k], cols[c])
        #   - If num is already present in any row, col, or subgrid, return false because this isn't a valid sudoku board.
        #   - If the loop finishes, return True because it is a valid sudoku board.
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != ".":
                    k = (r//3) * 3 + (c//3)
                    if num not in rows[r] and  num not in subgrids[k] and num not in cols[c]:
                        rows[r].add(num)
                        subgrids[k].add(num)
                        cols[c].add(num)
                    else:
                        return False
        return True
    
board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
sol = Solution()
print(sol.isValidSudoku(board))