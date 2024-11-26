"""
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Example 1:
Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Example 2:
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Example 3:
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
"""
from typing import List
from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Flatten the board into a tuple
        solvedState = '123450'
        state =''
        #state = ''.join(str(num) for row in board for num in row)  # Flatten and create a string
        for row in board:
            for num in row:
                state+=str(num)
        # BFS setup. Queue should track board state and number of moves to get to this state
        queue = deque([(state, 0, state.index('0'))])  # Queue stores (state, moves)
        visited = set()

        
        # Valid moves for each position on a 2x3 board
        # For example, if zero is at index 0 of the tuple, it can swap with the number at index 1 or index 3
        availableMoves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }
        # Iterate while there is something left in the queue
        while queue:
            board, moves, zeroIndex = queue.popleft()  # Dequeue the next state
            if board == solvedState:
                return moves  # Found the solution
            
            # Find the index of 0 (empty space) and generate neighbors
            for swap in availableMoves[zeroIndex]:
                newState = list(board)
                # Swap 0 with its neighbor
                newState[zeroIndex], newState[swap] = newState[swap], newState[zeroIndex]
                newState = ''.join(newState)  # Convert back to string
                
                # Check if this board state has been explored already, if it hasn't, add to queue and add to visited
                if newState not in visited:
                    visited.add(newState)  # Mark as visited
                    queue.append((newState, moves + 1, swap))  # Enqueue the new state
        
        return -1  # No solution


sol = Solution()
board = [[4,1,2],[5,0,3]]
print(sol.slidingPuzzle(board))    
"""
[[4,1,2]
,[5,0,3]]

"""    