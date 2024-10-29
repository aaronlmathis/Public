"""
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.
"""
from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]

        for col in range(cols - 2, -1, -1):
            for row in range(rows):
                curr_value = grid[row][col]

                for dr in [-1, 0, 1]:
                    new_row = row + dr
                    new_col = col + 1
                    if 0 <= new_row < rows and grid[new_row][new_col] > curr_value:
                        dp[row][col] = max(dp[row][col], 1 + dp[new_row][new_col])
        
        # Find the maximum moves starting from any cell in the first column
        max_moves = max(dp[row][0] for row in range(rows))

        return max_moves


sol = Solution()
grid = [[2,4,3,5],
        [5,4,9,3],
        [3,4,2,11],
        [10,9,13,15]]
print(sol.maxMoves(grid))
"""
DFS / Memoization Solution

        max_moves = 0
        rows, cols = len(grid), len(grid[0])
        memo = {}

        def max_value(row: int, col: int) -> int:
            if (row, col) in memo:
                return memo[(row, col)]

            curr = grid[row][col]

            max_count = 0
            for dr, dc in [(-1, 1), (0, 1), (1, 1)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and new_col < cols and grid[new_row][new_col] > curr:
                    max_count = max(max_count, 1 + max_value(new_row, new_col))                
            
            memo[(row, col)] = max_count
            
            return max_count
        
        for i in range(rows):
            max_moves = max(max_moves, max_value(i, 0))
        

        return max_moves

"""