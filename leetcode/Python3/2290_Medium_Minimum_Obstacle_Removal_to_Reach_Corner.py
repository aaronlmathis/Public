"""
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:
    - 0 represents an empty cell,
    - 1 represents an obstacle that may be removed.

You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.

Example 2:
Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
"""
from typing import List
import heapq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Possible Moves Right, Up, Left, Down
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # minHeap to return the move with least cost
        minHeap = [(0, 0, 0)]  # (currCost, row, col)

        # cost tracks the min cost to reach a cell
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0  # Starting point

        # Process grid
        while minHeap:
            currCost, row, col = heapq.heappop(minHeap)

            # If we reach the target cell
            if (row, col) == (m-1, n-1):
                return currCost

            # Process neighbors/moves and update cost
            for dr, dc in directions:
                nrow, ncol = row + dr, col + dc
                if 0 <= nrow < m and 0 <= ncol < n:
                    newCost = currCost + grid[nrow][ncol]
                    if newCost < cost[nrow][ncol]:
                        cost[nrow][ncol] = newCost
                        heapq.heappush(minHeap, (newCost, nrow, ncol))
        
        # Return cost to reach last cell
        return cost[m-1][n-1]
        

sol = Solution()
grid = [[0,1,1],
        [1,1,0],
        [1,1,0]]

print(sol.minimumObstacles(grid))        