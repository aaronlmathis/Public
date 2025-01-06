"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:


In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

"""
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return  # Empty board, nothing to do
                
        R = len(board)
        C = len(board[0])

        def dfs(y: int, x: int, board: List[List[str]]) -> None:
            if board[y][x] == "X":
                return
            board[y][x] = "S"


            if y + 1 < R and board[y+1][x] == "O" :
                dfs(y+1, x, board)
            if y - 1 >= 0 and board[y-1][x] == "O":
                dfs(y-1, x, board)
            if x + 1 < C and board[y][x+1] == "O":
                dfs(y, x+1, board)
            if x - 1 >= 0 and board[y][x-1] == "O":
                dfs(y, x-1, board)

        # Step 1: Mark all 'O's connected to the boundary as safe ('S')
        for y in range(R):
            for x in range(C):
                is_boundary = y == 0 or y == R - 1 or x == 0 or x == C - 1
                if is_boundary and board[y][x] == 'O':
                    dfs(y, x, board)

        # Step 2: Flip all remaining 'O's to 'X's and convert 'S' back to 'O's
        for y in range(R):
            for x in range(C):
                if board[y][x] == 'O':
                    board[y][x] = 'X'  # Capture surrounded region
                elif board[y][x] == 'S':
                    board[y][x] = 'O'  # Restore safe region


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol = Solution()
print(sol.solve(board))