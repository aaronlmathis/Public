"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 
"""
from collections import defaultdict, deque
import heapq
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build the graph: key is the source node, value is a list of tuples (price, destination)
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((p, t))
        
        # Priority queue: each element is a tuple (total_cost, current_node, stops)
        # We start at src with cost 0 and 0 stops.
        min_heap = [(0, src, 0)]  # cost, source node, stops
       
        # A dictionary to record the best (lowest) cost to reach a node with a given number of stops.
        # This helps prune states that are suboptimal.        
        explored = defaultdict(dict)

        while min_heap:
            curr_cost, curr_city, stops = heapq.heappop(min_heap)
            
            # If the destination is reached, return the current total cost.
            if curr_city == dst:
                return curr_cost
            
            # If we have exceeded the maximum allowed stops, skip further processing.            
            if stops > k:
                continue

            for price, next_dst in graph[curr_city]:
                next_cost = curr_cost + price
                next_stops = stops + 1
                
                # If we have seen a cheaper cost for the neighbor with the same number of stops, skip.
                if next_stops in explored[next_dst] and explored[next_dst][next_stops] <= next_cost:
                    continue
                
                explored[next_dst][next_stops] = next_cost
                heapq.heappush(min_heap, (next_cost, next_dst, next_stops))
        
        # The destination can't be reached in k stops
        return -1

#flights[i] = [fromi, toi, pricei]
sol = Solution()
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(sol.findCheapestPrice(n,flights,src,dst,k))