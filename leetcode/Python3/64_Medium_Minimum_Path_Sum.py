"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 
"""
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        dp = [[0 for _ in range(C)] for _ in range(R)]

        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:  # Start point
                    dp[i][j] = grid[i][j]
                elif i == 0:  # First row, only move from left
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:  # First column, only move from above
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:  # General case
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[R-1][C-1]

grid = [[1,2,3],[4,5,6]]
sol = Solution()
print(sol.minPathSum(grid))        