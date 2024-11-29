"""
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

Example 1:
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

Example 2:
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
"""
from typing import List
from collections import deque, defaultdict
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # edge = [from, to, weight]
        adj = defaultdict(list) # from: [(to, distance), (to, distance)]
        for start, dest, dist in edges:
            adj[start].append((dest, dist))
            adj[dest].append((start, dist))
        
        def djikstra(start):
            distances = [float('inf')] * n
            distances[start] = 0
            queue = [(0, start)] # (currDist, currNode)
    
            while queue:
                currDist, currNode = heapq.heappop(queue)
                
                if currDist > distances[currNode]:
                    continue

                for dest, dist in adj[currNode]:
                    newDist = currDist + dist
                    if newDist < distances[dest]:
                        distances[dest] = newDist
                        heapq.heappush(queue, (newDist, dest))

            return sum(1 for d in distances if d <= distanceThreshold)
        
        result = (float('inf'), -1)
        for i in range(n):
            reachable = djikstra(i)
            if reachable < result[0] or (reachable == result[0] and i > result[1]):
                result = (reachable, i)
        
        return result[1]
        
n = 4
edges = [
    [0,1,3],
    [1,2,1],
    [1,3,4],
    [2,3,1]
         ]
distanceThreshold = 4        
sol = Solution()
print(sol.findTheCity(n, edges, distanceThreshold))