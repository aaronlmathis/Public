"""
You are given an array start where start = [startX, startY] represents your initial position (startX, startY) in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position (targetX, targetY).

The cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.

There are also some special roads. You are given a 2D array specialRoads where specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road goes in one direction from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use each special road any number of times.

Return the minimum cost required to go from (startX, startY) to (targetX, targetY).

Example 1:
Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
Output: 5
Explanation:
(1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1.
(1,2) to (3,3). Use specialRoads[0] with the cost 2.
(3,3) to (3,4) with a cost of |3 - 3| + |4 - 3| = 1.
(3,4) to (4,5). Use specialRoads[1] with the cost 1.
So the total cost is 1 + 2 + 1 + 1 = 5.

Example 2:
Input: start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
Output: 7
Explanation:
It is optimal not to use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7.
Note that the specialRoads[0] is directed from (5,7) to (3,2).

Example 3:
Input: start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]
Output: 8
Explanation:
(1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1.
(1,2) to (7,4). Use specialRoads[1] with the cost 4.
(7,4) to (10,4) with a cost of |10 - 7| + |4 - 4| = 3.
"""
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"{fname} took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper

from heapq import heappop, heappush
from typing import List

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        # Convert start and target to tuples for consistency in dictionary keys
        start, target = tuple(start), tuple(target)

        # Compute direct Manhattan distance from start to target (reference distance)
        refD = abs(target[0] - start[0]) + abs(target[1] - start[1])

        # Filter out special roads where the special cost is greater than or equal to direct Manhattan cost
        filtered_roads = [
            (x1, y1, x2, y2, c) 
            for x1, y1, x2, y2, c in specialRoads 
            if c < abs(x2 - x1) + abs(y2 - y1)
        ]
        
        # Add an identity road to allow direct movement
        filtered_roads.append((*start, *start, 0))

        # Priority queue (Min-Heap) for Dijkstra’s traversal, starting from target
        pq = [(0, target[0], target[1])]

        # Set to track visited nodes
        seen = set()

        # Process the priority queue
        while pq:
            cost, x, y = heappop(pq)

            # If we reach the start, return the total cost
            if (x, y) == start:
                return cost
            
            # Skip if already processed
            if (x, y) in seen:
                continue
            
            # Mark the node as visited
            seen.add((x, y))

            # Traverse valid special roads and compute new costs
            for x1, y1, x2, y2, c in filtered_roads:
                new_cost = cost + c + abs(x2 - x) + abs(y2 - y)

                # Only push into heap if within the reference distance
                if new_cost <= refD:
                    heappush(pq, (new_cost, x1, y1))

        # If no valid path found, return -1
        return -1


sol = Solution()
start = [1,1]
target = [4,5]
specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
print(sol.minimumCost(start,target,specialRoads))
start = [3,2]
target = [5,7]
specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
print(sol.minimumCost(start,target,specialRoads))
start = [1,1]
target = [10,4]
specialRoads =[[4,2,1,1,3],     #(4,2)->(1,1)
               [1,2,7,4,4],     #(1,2)->(7,4)
               [10,3,6,1,2],    #(10,3)->(6,1)
               [6,1,1,2,3]]     #(6,1)->(1,2)

print(sol.minimumCost(start,target,specialRoads))
start = [1,1]
target = [4, 6]
specialRoads = [[3,4,2,4,1],[2,5,4,2,5],[3,2,1,6,3]]

print(sol.minimumCost(start,target,specialRoads))