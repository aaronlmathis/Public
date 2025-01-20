"""
Given an m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:

1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some signs on the cells of the grid that point outside the grid.

You will initially start at the upper left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path does not have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

Example 1:
Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.

Example 2:
Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).

Example 3:
Input: grid = [[1,2],[4,3]]
Output: 1
"""
from typing import Optional, List
from collections import deque
import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        # Distance Matrix where dist[n][m] = cost to reach grid[n][m]
        cost = [[float('inf')] * m for _ in range(n)]
        cost[0][0] = 0

      
        directions = [
            (0, 1, 1),      # Right
            (0, -1, 2),     # Left
            (1, 0, 3),     # Down
            (-1, 0, 4)       # Up
        ]

        # Create a deque for BFS 0-1 traversal
        queue = deque([(0,0)]) #  ((i, j)

        # Iterate while queue isn't empty
        while queue:
            # Pop the top of the queue
            i, j = queue.popleft()
            # Iterate over all possible moves (within bounds)
            for di, dj, d_code in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:            
                    # Calculate the cost to get to this adjacent cell, 0 cost if direction is the same
                    new_cost = cost[i][j] + (0 if grid[i][j] == d_code else 1)
                    # Check to see if new cost is less than the current lowest cost to reach ni, nj
                    # If it is, set the new cost in cost[ni][nj]
                    if new_cost < cost[ni][nj]:
                        cost[ni][nj] = new_cost
                        # If no cost was incurred, add to the left; otherwise, add to the right.
                        # This ensures the lower cost option is evaluated first.
                        if grid[i][j] == d_code:
                            queue.appendleft((ni, nj))
                        else:
                            queue.append((ni, nj))
        # Return the cost
        return cost[n-1][m-1]

# Right - Left - Down - Up / 1234
sol = Solution()
grid = [[1,1,1,1],
        [2,2,2,2],
        [1,1,1,1],
        [2,2,2,2]] 
#grid = [[1,1,3],[3,2,2],[1,1,4]]       
#grid = [[1,2],[4,3]]
print(sol.minCost(grid))