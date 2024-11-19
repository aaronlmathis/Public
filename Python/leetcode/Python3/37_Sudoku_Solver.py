"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Define the size of the board
        N = len(board)
        
        # Bitmasks for rows, columns, and boxes
        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N
        
        # Convert (row, col) to box index
        def getBoxIndex(row, col):
            return (row // 3) * 3 + (col // 3)
        
        # Initialize the bitmasks with current board values
        empty_cells = []
        for row in range(N):
            for col in range(N):
                if board[row][col] == '.':
                    empty_cells.append((row, col))
                else:
                    num = int(board[row][col])
                    bitmask = 1 << (num - 1)
                    rows[row] |= bitmask
                    cols[col] |= bitmask
                    boxes[getBoxIndex(row, col)] |= bitmask
        
        # Helper function to check if a number can be placed
        def couldPlace(num, row, col):
            bitmask = 1 << (num - 1)
            return not (rows[row] & bitmask or cols[col] & bitmask or boxes[getBoxIndex(row, col)] & bitmask)
        
        # Place a number in the cell
        def placeNumber(num, row, col):
            bitmask = 1 << (num - 1)
            board[row][col] = str(num)
            rows[row] |= bitmask
            cols[col] |= bitmask
            boxes[getBoxIndex(row, col)] |= bitmask
        
        # Remove a number from the cell
        def removeNumber(num, row, col):
            bitmask = ~(1 << (num - 1))
            board[row][col] = '.'
            rows[row] &= bitmask
            cols[col] &= bitmask
            boxes[getBoxIndex(row, col)] &= bitmask
        
        # Backtracking function
        def backtrack(index):
            if index == len(empty_cells):
                return True
            
            row, col = empty_cells[index]
            for num in range(1, 10):
                if couldPlace(num, row, col):
                    placeNumber(num, row, col)
                    if backtrack(index + 1):
                        return True
                    removeNumber(num, row, col)
            
            return False
        
        # Start backtracking from the first empty cell
        backtrack(0)

sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(sol.solveSudoku(board))
print(board)