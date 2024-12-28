"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])

        def dfs(y: int, x: int, grid: List[List[str]]) -> None:

            # Base cases: check for out-of-bounds indices or water cells
            if y < 0 or y >= R or x < 0 or x >= C or grid[y][x] == '0':
                return

            grid[y][x] = "0"

            if y + 1 < R and grid[y+1][x] == "1":
                dfs(y+1, x, grid)
            if y - 1 >= 0 and grid[y-1][x] == "1":
                dfs(y-1, x, grid)
            if x + 1 < C and grid[y][x+1] == "1":
                dfs(y, x+1, grid)
            if x - 1 >= 0 and grid[y][x-1] == "1":
                dfs(y, x-1, grid)                
                                        
            
        island_count = 0
        for y in range(R):
            for x in range(C):
                if grid[y][x] == "1":
                    island_count+=1
                    dfs(y, x, grid)
        return island_count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
sol = Solution()
print(sol.numIslands(grid))
