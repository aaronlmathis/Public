"""
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 
"""
from typing import List
from collections import deque, defaultdict
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        n = len(heightMap)
        m = len(heightMap[0])
        
        # Quick exit - if the length or width of map is <=2, it can't hold water.
        if n <=2 or m <=2:
            return 0
        
        # Potential neighbors
        dir = [(-1,0), (0, 1), (1,0), (0, -1)]

        # Keep a set to track visited and initialize a list for a priority queue
        visited = set()
        pq = []

        # Track total water
        total_water = 0

        # Add all border cells to the priority queue (min-heap)... (height, row, col).
        # Also add the border cells to the visited set

        for i in range(m):
            heapq.heappush(pq, (heightMap[0][i], 0, i))
            visited.add((0, i))
            heapq.heappush(pq, (heightMap[n-1][i], n-1, i))
            visited.add((n-1, i))

        for i in range(1, n-1):
            heapq.heappush(pq, (heightMap[i][0], i, 0))
            visited.add((i,0))
            heapq.heappush(pq, (heightMap[i][m-1], i, m-1))
            visited.add((i, m-1))

        # Process the min-heap using BFS-like traversal.
        # Popping from the pq will give you the cell with the shortest height.
        while pq:
            
            height, r, c = heapq.heappop(pq)
            
            # Process the cell's neighbors, making sure to stay in bounds and not process cells already visited
            for y, x in dir:
                nr, nc = r+y, c+x
                if (nr, nc) in visited or nr > n-1 or nc > m-1 or nr < 0 or nc < 0:
                    continue

                # Add the neighbor cell to the visited set
                visited.add((nr, nc))
                
                # Calculate the height of the neighbor as well as its new height
                neigh_height = heightMap[nr][nc]
                new_nei_height = max(neigh_height, height)

                # Calculate how much water can be in this cell if any. Add it to the total water.
                water = max(0, height - neigh_height)
                total_water += water
                              
                # Push the neighbor, with it's adjusted height
                heapq.heappush(pq, (new_nei_height, nr, nc))     
        
        # Return the total water
        return total_water


"""
        water = 0
        # Iterate through cells not on outer wall.
        for i in range(1, n-1):
            for j in range(1, m-1):
                height = heightMap[i][j]
                # top
                max_top, max_bottom, max_left, max_right = float('-inf'),float('-inf'),float('-inf'),float('-inf')
                t,b = i, i
                r,l = j, j
                while t > 0:
                    max_top = max(max_top, heightMap[t-1][j])
                    t-=1
                print(f"At ({i}, {j}) max_top is {max_top}")

                while b < n-1:
                    max_bottom = max(max_bottom, heightMap[b+1][j])
                    b+=1
                print(f"At ({i}, {j}) max_bottom is {max_bottom}")
                
                while l > 0:
                    max_left = max(max_left, heightMap[i][l-1])
                    l-=1
                print(f"At ({i}, {j}) max_left is {max_left}")

                while r < m-1:
                    max_right = max(max_right, heightMap[i][r+1])
                    r+=1
                print(f"At ({i}, {j}) max_right is {max_right}")                    
                print()

                if max_top > height and max_bottom > height and max_left > height and max_right > height:
                    water+= min(max_top, max_bottom, max_left, max_right) - height
                    print(f"{water} units of water!")
        return water
"""
heightMap = [[1,4,3,1,3,2],
             [3,2,1,3,2,4],
             [2,3,3,2,3,1]]

heightMap = [[3,3,3,3,3],
             [3,2,2,2,3],
             [3,2,1,2,3],
             [3,2,2,2,3],
             [3,3,3,3,3]]

heightMap = [[12,13,1,12],
             [13,4,13,12],
             [13,8,10,12],
             [12,13,12,12],
             [13,13,13,13]]
sol = Solution()
print(sol.trapRainWater(heightMap))