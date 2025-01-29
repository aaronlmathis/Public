"""
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

Example 1:


Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
0 <= grid[i][j] <= 10

class UnionFind:
    def __init__(self, n) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def join(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

from typing import List
from collections import defaultdict

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        grid_1D = [grid[r][c] for r in range(m) for c in range(n)]
        print(grid_1D)
        nn = len(grid_1D)
        union = UnionFind(nn)
        # Up:       idx - n
        # Down:     idx + n
        # Left:     idx -1 
        # Right:    idx + 1
        for cell in range(nn):
            if grid_1D[cell] == 0:  
                continue

            if cell - n >= 0 and grid_1D[cell-n] != 0:
                union.join(cell, cell-n)
            if cell + n < nn and grid_1D[cell+n] != 0:
                union.join(cell, cell+n)
            if cell % n != 0 and grid_1D[cell - 1] != 0:
                union.join(cell, cell-1)
            if (cell + 1) % n != 0 and grid_1D[cell + 1] != 0:
                union.join(cell, cell+1)
        
        fish_count = defaultdict(int)
        
        for cell in range(nn):
            if grid_1D[cell] > 0:
                root = union.find(cell)
                fish_count[root] += grid_1D[cell]
        

        return max(fish_count.values()) if len(fish_count) > 0 else 0
"""

from typing import List
from collections import defaultdict

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))
            fish_count = grid[r][c]

            fish_count+=dfs(r+1, c)
            fish_count+=dfs(r-1, c)
            fish_count+=dfs(r, c+1)
            fish_count+=dfs(r, c-1)
            
            return fish_count
                
        m = len(grid)
        n = len(grid[0])

        # Track Visited cells and max fish count
        visited = set()
        max_fish = 0
        # Iterate through cells looking for water that hasn't been visited.
        # If found, use DFS traversal to find all fish in body of water.
        # Compare total fish found to the max fish count tracked        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i, j) not in visited:
                    max_fish = max(dfs(i, j), max_fish)
        
        return max_fish
    
sol = Solution()
grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
#grid = [[0, 4]]
grid = [[10,5],
        [8,0]]
print(sol.findMaxFish(grid))