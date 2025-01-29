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
import time
def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after =  time.time()
        fname = function.__name__
        print(f"{fname} took {round(after-before, 3)} seconds to execute!")
        return value
    return wrapper

from typing import List

class Solution:
    @timed
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        def find(x: int) -> None:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x: int, y: int) -> bool:
            rootX = find(x)
            rootY = find(y)
            # Connect
            if rank[rootX] >= rank[rootY]:
                parent[rootX] = rootY
                rank[rootX] += rank[rootY]
            else:
                parent[rootY] = rootX
                rank[rootY] += rank[rootX]
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        return []

sol = Solution()
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(sol.findRedundantConnection(edges))