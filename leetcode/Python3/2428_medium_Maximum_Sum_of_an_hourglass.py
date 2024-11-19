"""
You are given an m x n integer matrix grid.
"""
from typing import List
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = float('-inf')  # Start with the smallest possible value
    
        # Traverse the grid, ensuring there's space for a 3x3 hourglass
        for i in range(len(grid) - 2):         # i goes up to len(grid) - 3
            for j in range(len(grid[0]) - 2):  # j goes up to len(grid[0]) - 3
                hourglass = (grid[i][j] + grid[i][j+1] + grid[i][j+2]) + (grid[i+1][j+1]) + (grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2])
                max_sum = max(max_sum, hourglass)
        return max_sum
    
grid = [
    [6,2,1,3],
    [4,2,1,5],
    [9,2,8,7],
    [4,1,2,9]
]
sol = Solution()
print(sol.maxSum(grid))