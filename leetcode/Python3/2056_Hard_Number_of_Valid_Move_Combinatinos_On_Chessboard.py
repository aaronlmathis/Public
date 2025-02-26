"""
There is an 8 x 8 chessboard containing n pieces (rooks, queens, or bishops). You are given a string array pieces of length n, where pieces[i] describes the type (rook, queen, or bishop) of the ith piece. In addition, you are given a 2D integer array positions also of length n, where positions[i] = [ri, ci] indicates that the ith piece is currently at the 1-based coordinate (ri, ci) on the chessboard.

When making a move for a piece, you choose a destination square that the piece will travel toward and stop on.

A rook can only travel horizontally or vertically from (r, c) to the direction of (r+1, c), (r-1, c), (r, c+1), or (r, c-1).
A queen can only travel horizontally, vertically, or diagonally from (r, c) to the direction of (r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1).
A bishop can only travel diagonally from (r, c) to the direction of (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1).
You must make a move for every piece on the board simultaneously. A move combination consists of all the moves performed on all the given pieces. Every second, each piece will instantaneously travel one square towards their destination if they are not already at it. All pieces start traveling at the 0th second. A move combination is invalid if, at a given time, two or more pieces occupy the same square.

Return the number of valid move combinations​​​​​.

Notes:

No two pieces will start in the same square.
You may choose the square a piece is already on as its destination.
If two pieces are directly adjacent to each other, it is valid for them to move past each other and swap positions in one second.
Example 1:


Input: pieces = ["rook"], positions = [[1,1]]
Output: 15
Explanation: The image above shows the possible squares the piece can move to.
Example 2:


Input: pieces = ["queen"], positions = [[1,1]]
Output: 22
Explanation: The image above shows the possible squares the piece can move to.
Example 3:


Input: pieces = ["bishop"], positions = [[4,3]]
Output: 12
Explanation: The image above shows the possible squares the piece can move to.
 

Constraints:

n == pieces.length 
n == positions.length
1 <= n <= 4
pieces only contains the strings "rook", "queen", and "bishop".
There will be at most one queen on the chessboard.
1 <= ri, ci <= 8
Each positions[i] is distinct.
"""
from typing import List

from typing import List
from itertools import product

class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        n = len(pieces)
        comb_moves = self.get_comb_moves(pieces)
        board = [(x - 1, y - 1) for x, y in positions]

        ans = set()
        for move in comb_moves:
            self.dfs(move, n, board, (1 << n) - 1, ans)

        return len(ans)

    def get_comb_moves(self, pieces: List[str]) -> List[List[tuple]]:
        pieces_move = [self.get_move(piece) for piece in pieces]
        return list(product(*pieces_move))

    def get_move(self, piece: str) -> List[tuple]:
        moves = {"rook": [(1, 0), (-1, 0), (0, 1), (0, -1)], 
                 "bishop": [(1, 1), (1, -1), (-1, 1), (-1, -1)],
                 "queen": [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]}
        return moves[piece]

    def dfs(self, move: List[tuple], n: int, board: List[tuple], active_mask: int, ans: set):
        if active_mask == 0:
            return
        
        ans.add(self.hash(board))
        for next_active_mask in range(1, 1 << n):
            if not (active_mask & next_active_mask):
                continue
            
            # Make a copy of the board
            next_board = list(board)

            # Move active pieces
            for i in range(n):
                if (next_active_mask >> i) & 1:
                    next_board[i] = (next_board[i][0] + move[i][0], next_board[i][1] + move[i][1])

            # Check the validity of the new configuration
            if self.is_valid(next_board):
                self.dfs(move, n, next_board, next_active_mask, ans)

    def is_valid(self, board: List[tuple]) -> bool:
        # Check boundary and uniquness of the positions
        positions = set()
        for x, y in board:
            if x < 0 or x >= 8 or y < 0 or y >= 8:
                return False
            if (x, y) in positions:
                return False
            positions.add((x, y))
        return True

    def hash(self, board: List[tuple]) -> int:
        hashed = 0
        for x, y in board:
            hashed = hashed * 64 + x * 8 + y
        return hashed
sol = Solution()
pieces = ["rook"]
positions = [[1,1]]
print(sol.countCombinations(pieces, positions))