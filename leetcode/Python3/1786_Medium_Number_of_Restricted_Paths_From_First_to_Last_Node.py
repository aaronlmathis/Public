"""
There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.

Example 1:
Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
Output: 3
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5

Example 2:
Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
Output: 1
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The only restricted path is 1 --> 3 --> 7.

Constraints:

1 <= n <= 2 * 104
n - 1 <= edges.length <= 4 * 104
edges[i].length == 3
1 <= ui, vi <= n
ui != vi
1 <= weighti <= 105
There is at most one edge between any two nodes.
There is at least one path between any two nodes.
"""
from typing import List
from collections import deque, defaultdict
from heapq import *
from math import inf
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7 # Return MOD of answer

        # Build Undirected Graph where graph[node_a] -> (weight, node_b) shows a connection
        graph = {x:[] for x in range(1, n+1)}
        for u, v, weight in edges:
            graph[u].append((weight, v))
            graph[v].append((weight, u))

        # Distance array to track shortest distance from starting node to node at index i
        distance = [inf] * (n+1)
        distance[n] = 0

        # DP array for Memoization of number of paths from 1-n
        dp = [0] * (n+1)
        dp[n] = 1

        # Combine Dijkstra's formula (min heap + BFS) with DP

        pq = [(0, n)]   # Priority Queue (min-heap) for BFS
        # Process pq
        while pq:
            # Get the node with the smallest distance
            weight, node = heappop(pq)
            
            # If the current path is longer than already known path to node, move on
            if weight > distance[node]:
                continue
            
            # Process next node's, updating the distance to next node if smaller than currently known paths.
            # If a shorter path is found, add the next node to min-heap/pq to process further.
            # If current path distance is greater than shortest path to neighbor, update dp table
            for nweight, nnode in graph[node]:
                new_weight = nweight + distance[node]
                if new_weight < distance[nnode]:
                    distance[nnode] = new_weight
                    heappush(pq, (new_weight, nnode))
                elif weight > distance[nnode]:
                    dp[node] = (dp[node] + dp[nnode]) % MOD
        
            if node == 1:
                break
        
        return dp[1]
        # Rebuild (directed) Graph now that we know shortest paths so that DFS is much more efficient.
        dag = defaultdict(list)
        for u in range(1, n+1):
            for w, v in graph[u]:
                if distance[u] > distance[v]:
                    dag[u].append(v)

        dp = {}

        # Use Dynamic Programming + DFS to determine number of restricted paths from 1-n in a DAG
        return find_restricted_paths(1) 
        

        
sol = Solution()
n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
print(sol.countRestrictedPaths(n, edges))
n = 7
edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
#print(sol.countRestrictedPaths(n, edges))