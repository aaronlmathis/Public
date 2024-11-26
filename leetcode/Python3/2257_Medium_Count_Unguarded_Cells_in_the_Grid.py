"""
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

 

Example 1:


Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:


Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
"""
from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Populate seen matrix with O's
        seen =[['O' for _ in range(n)] for _ in range(m)]
        # Initialize count
        count = 0
        # Add walls to seen matrix, increase count
        for wall in walls:
            seen[wall[0]][wall[1]] = 'WL'
            count+=1
    
        # Add Guards to seen matrix, increase count
        for guard in guards:
            seen[guard[0]][guard[1]] = 'GD'
            count+=1 

        # Iterate through each grid location, checking to see if a guard is present.
        # If guard is present, iterate north, south, east, and west marking the location XX if not already
        # and increasing the count -- unless you find another guard or wall
        for y in range(m):
            for x in range(n):
                if seen[y][x] == 'GD':
                    left, right = x - 1, x + 1
                    while right <= n-1 and (seen[y][right] != 'WL' and seen[y][right] != 'GD'):
                        if seen[y][right] != 'XX':
                            seen[y][right] = 'XX'
                            count+=1
                        right+=1

                    while left >= 0 and (seen[y][left] != 'WL' and seen[y][left] != 'GD'):
                        if seen[y][left] != 'XX':
                            seen[y][left] = 'XX'
                            count+=1                        
                        left-=1
                    
                    up, down = y-1, y+1

                    while up >= 0 and (seen[up][x] != 'WL' and seen[up][x] != 'GD'):
                        if seen[up][x] != 'XX':                        
                            seen[up][x] = 'XX'
                            count+=1                        
                        up-=1


                    while down <= m-1 and (seen[down][x] != 'WL' and seen[down][x] != 'GD'):
                        if seen[down][x] != 'XX':
                            seen[down][x] = 'XX'
                            count+=1                        
                        down+=1
        # Return m * n (the total grid location count) minus the count
        # This will be equal to all the unguarded spots.
        return (m*n) - count

m = 2
n = 7
guards = [[1,5],[1,1],[1,6],[0,2]]
walls = [[0,6],[0,3],[0,5]]    
sol = Solution()
print(sol.countUnguarded(m,n,guards,walls))