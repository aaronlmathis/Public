"""
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""
from collections import deque
from typing import List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        result = 0
        m = len(grid)
        for i in range(m):
            row_sum = sum(grid[i])
            if row_sum > 1:
                result+=row_sum
                continue
            elif row_sum == 1:
                column_sum = 0
                column = grid[i].index(1)
                for j in range(m):
                    column_sum+= grid[j][column]
                    if column_sum > 1:
                        result+=1
                        break
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        m, n = len(grid), len(grid[0])
        r, c = [0] * m, [0] * n
        servers = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    r[i]+=1
                    c[j]+=1
                    servers.add((i, j))

        isolated=0
        for sr, sc in servers:
            if r[sr] == 1 and c[sc] == 1:
                isolated+=1


        return len(servers) - isolated


        return servers
sol = Solution()
grid = [[1,1,0,0],
        [0,0,1,0],
        [0,0,1,0],
        [0,0,0,1]]
print(sol.countServers(grid))