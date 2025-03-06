"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
"""
from typing import List
from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        disc = [-1] * n
        low = [-1] * n
        res = []
        time = 0

        def dfs(node, parent):
            nonlocal time
            disc[node] = low[node] = time
            time+=1

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if disc[neighbor] == -1:
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > disc[node]:
                        res.append([node, neighbor])
                else:
                    low[node] = min(low[node], disc[neighbor])
        dfs(0,-1)
        return res
sol = Solution()
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]    
print(sol.criticalConnections(n, connections))