"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        minutes = 0        # Track minutes, intialize as -1
        queue = deque()     # Our queue of rotten oranges.

        fresh_oranges = 0   # Track number of fresh oranges.

        # Multi-Source BFS requires identifying starting nodes. Find rotten oranges, count fresh oranges
        for row in range(R):
            for col in range(C):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1
        
        # Exit if there are no fresh oranges
        if fresh_oranges == 0:
            return 0
        
        # Process `queue`, level by level. Each iteration is 1 minute.
        while queue:
            # To process entire queue each iteration, we need to loop through every item currently in `queue`.
            for _ in range(len(queue)):
                curr_row, curr_col = queue.popleft()

                # Check boundaries and then for the presence of fresh orange in all 4 directions.
                # If found, add to queue and mark as rotten on `grid`. Decrese `fresh_oranges`

                for i, j in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nrow = curr_row+i
                    ncol = curr_col+j
                    if (0 <= nrow < R and 0 <= ncol < C) and grid[nrow][ncol] == 1:
                        queue.append((nrow, ncol))
                        grid[nrow][ncol] = 2
                        fresh_oranges-=1
           
            # At the end of this iteration of `queue`, a minute as passed. Increase `minutes`
            if queue:
                minutes += 1
        
        # Return `minutes` unless there are still fresh oranges
        return minutes if fresh_oranges == 0 else -1
    
sol = Solution()
grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]
print(sol.orangesRotting(grid))        