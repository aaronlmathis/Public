"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.

Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
"""
from typing import List
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]])-> int:
        def getPosition(square:int)-> tuple: #(row, col)
            """
            getPosition(square) returns the (row, col) of the board when given a square
            """
            row = n - 1 - (square - 1) // n
            col = (square - 1) % n if (n - row) % 2 == 1 else n - 1 - (square - 1) % n
            return (row, col)
        
        n = len(board)  
        end = (n*n) # Last square
        q = deque([(1, 0)]) # Queue for BFS - square / rolls
        visited = set([1]) # Visited set showing squares visited already
        
        # BFS
        while q:
            # Pop square/rolls from queue
            current, rolls = q.popleft()
            # Terminate if current equals end (game is won) and return how many rolls it took
            if current == end:
                return rolls
            # Simulate 6 sided dice roll
            for i in range(1, 7):
                # Destination square
                destination = current+i
                # Out of bounds, ignore
                if destination > end:
                    continue
                # Get the board coordinates for that destination square
                y, x = getPosition(destination)
                nextSquare = board[y][x]
                # Check for snakes/ladders.
                # If snake or ladder, update the destination with what is listed in the board
                if nextSquare != -1:
                    destination = nextSquare
                if destination not in visited:
                    q.append((destination, rolls + 1))
                    visited.add(destination)
  
        # End was never reached and every square has been visited
        return -1

        
sol = Solution()
board = [[-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,35,-1,-1,13,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,15,-1,-1,-1,-1]]

print(sol.snakesAndLadders(board))