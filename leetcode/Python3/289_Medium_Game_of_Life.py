"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.
"""
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R = len(board)
        C = len(board[0])
        
        nextState = [0] * (R*C) # 1D Flattened 2D matrix to store next state of each cell after iteration
        
        # Neighbors Top, Right, Bottom, Left, Top-Right, Bottom-Left, Bottom-Right, Top-Left
        nb = ((-1,0), (0,1), (1,0), (0,-1), (1, 1), (-1, -1), (-1, 1), (1, -1))

        # currCell (0 - (R*C))
        currCell = 0

        for r, row in enumerate(board):
            for c, col in enumerate(row):
                ncount = 0
                for nrow, ncol in nb:
                    newr = nrow + r
                    newc = ncol + c
                    if (newr >= 0 and newr < R) and (newc >= 0 and newc < C):
                        ncount+=board[newr][newc]
                
                if board[r][c] == 1: # If current cell is alive
                    if ncount < 2:
                        nextState[currCell] = 0
                    elif ncount <= 3:
                        nextState[currCell] = 1
                    else:
                        nextState[currCell] = 0
                else:   # If current cell isn't alive
                    if ncount == 3:
                        nextState[currCell] = 1
                # Move to the next cell
                currCell += 1 

        currCell = 0

        for r, row in enumerate(board):
            for c, col in enumerate(row):
                board[r][c] = nextState[currCell]
                currCell+=1

        return board
sol = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(f"Actual: {sol.gameOfLife(board)}")
print( "Expect: [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]")
"""
[[0,1,0],
 [0,0,1],
 [1,1,1],
 [0,0,0]]
"""