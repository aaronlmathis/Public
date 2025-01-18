"""
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 
"""
from typing import List
from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Dictionary to keep track of parent pointers
        parent = {}

        def find(x):
            # Initialize the parent if not present
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            # Find the leaders (parents) for x and y
            rootX, rootY = find(x), find(y)
            # If they are already connected, the edge (x, y) is redundant
            if rootX == rootY:
                return False
            # Union the sets by connecting the roots
            parent[rootX] = rootY
            return True

        # Process each edge
        for u, v in edges:
            # If a node is not in parent dictionary, initialize it
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v

            # If union returns False, we've found the redundant edge
            if not union(u, v):
                return [u, v]

sol = Solution()
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(sol.findRedundantConnection(edges))