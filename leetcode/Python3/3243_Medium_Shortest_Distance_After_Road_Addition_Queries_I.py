"""
You are given an integer n and a 2D integer array queries.
There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.
queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.
Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

Example 1:
Input: n = 5, queries = [[2,4],[0,2],[0,4]]
Output: [3,2,1]
Explanation:

Example 2:
Input: n = 4, queries = [[0,3],[0,2]]
Output: [1,1]
Explanation:
"""
from typing import List
from collections import deque, defaultdict
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Create an adjacency list to represent the graph
        adjacentList = defaultdict(list)
        # Initialize the adjacency list with direct connections (0 -> 1 -> 2 -> ... -> n-1)
        for i in range(n-1):
            adjacentList[i].append(i+1)

        # Initialize the depth array, where depth[i] represents the shortest distance from node 0 to node i
        depth = [i for i in range(n)]

        def bfs(node):
            """
            Breadth-First Search to update depths starting from the given node.
            If a shorter path to any node is found, update its depth.
            """
            q = deque([node])  # Initialize the queue with the starting node
            while q:
                n = q.popleft()  # Dequeue a node
                for nei in adjacentList[n]:  # Iterate through its neighbors
                    # If a shorter path to the neighbor is found, update its depth
                    if depth[nei] > depth[n] + 1:
                        depth[nei] = depth[n] + 1
                        q.append(nei)  # Enqueue the neighbor for further processing

        answer = []
        for start, end in queries:
            # Add the new edge from start to end
            adjacentList[start].append(end)
            # If this new edge creates a shorter path, update the depth and run BFS
            if depth[end] > depth[start] + 1:
                depth[end] = depth[start] + 1
                bfs(end)  # Propagate the depth update to other nodes
            
            # Append the shortest distance to the last node (n-1) after processing the query
            answer.append(depth[-1])

        return answer

                    
       



sol = Solution()
n = 5
queries = [[2,4],[0,2],[0,4]]
print(sol.shortestDistanceAfterQueries(n,queries))