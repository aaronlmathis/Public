"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.


Example 1:
Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]

Example 2:
Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]

Constraints:
1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
"""
from collections import deque, defaultdict
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # Graph construction
        graph = [defaultdict(list), defaultdict(list)]  # graph[0] for red, graph[1] for blue
        for a, b in redEdges:
            graph[0][a].append(b)
        for a, b in blueEdges:
            graph[1][a].append(b)

        # Distance table: dist[node][color] -> shortest path using last edge as `color`
        dist = [[float('inf')] * 2 for _ in range(n)]
        dist[0] = [0, 0]  # Distance from node 0 to itself is 0 for both colors

        # Multi-source BFS (start from node 0 with both red and blue edges)
        queue = deque([(0, 0), (0, 1)])  # (node, color) where 0 = red, 1 = blue
        
        while queue:
            node, color = queue.popleft()
            next_color = 1 - color  # Alternate the edge color

            for neighbor in graph[next_color][node]:
                if dist[neighbor][next_color] == float('inf'):  # Unvisited via this color
                    dist[neighbor][next_color] = dist[node][color] + 1
                    queue.append((neighbor, next_color))

        # Construct the result: take the minimum of red and blue paths
        return [min(dist[i]) if min(dist[i]) != float('inf') else -1 for i in range(n)]


sol = Solution()

n = 3
redEdges = [[0,1],[1,2]]
blueEdges = []        
print(sol.shortestAlternatingPaths(n, redEdges, blueEdges))
n = 5
redEdges =[[0,1],[1,2],[2,3],[3,4]]
blueEdges =[[1,2],[2,3],[3,1]]
#[0,1,2,3,7]
n =5
redEdges =[[2,0],[4,3],[4,4],[3,0],[1,4]]
blueEdges =[[2,1],[4,3],[3,1],[3,0],[1,1],[2,0],[0,3],[3,3],[2,3]]
print(sol.shortestAlternatingPaths(n, redEdges, blueEdges))
n =5
redEdges =[[2,2],[0,1],[0,3],[0,0],[0,4],[2,1],[2,0],[1,4],[3,4]]
blueEdges =[[1,3],[0,0],[0,3],[4,2],[1,0]]
#[0,1,2,1,1]
print(sol.shortestAlternatingPaths(n, redEdges, blueEdges))