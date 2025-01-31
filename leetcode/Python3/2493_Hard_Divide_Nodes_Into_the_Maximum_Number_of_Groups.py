"""
You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

 

Example 1:


Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
Output: 4
Explanation: As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.
Example 2:

Input: n = 3, edges = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy the first two edges, we can see that the third edge will not be satisfied.
It can be shown that no grouping is possible.
 

Constraints:

1 <= n <= 500
1 <= edges.length <= 104
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
There is at most one edge between any pair of vertices.
"""
from typing import List
from collections import deque, defaultdict

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjacency list for the graph
        self.adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            # Convert to zero-based index
            self.adj[v1 - 1].append(v2 - 1)
            self.adj[v2 - 1].append(v1 - 1)

        # List to hold all connected components
        self.components = []
        self.fill_components(n)

        # Total count for all components
        total_ans = 0
        for comp in self.components:
            # Answer for the current component
            comp_ans = 0
            # Check if the component is bipartite
            if self.bipartite_check(comp[0], comp):
                for i in range(len(comp)):
                    comp_ans = max(comp_ans, self.bfs(comp[i], n))
                total_ans += comp_ans
            else:
                # Return -1 if the component is not bipartite
                return -1
        # Return the total count for all components
        return total_ans

    def fill_components(self, n: int):
        # Initialize visited list to track visited nodes
        visited = [False] * n
        def bfs(start):
            # Perform BFS to find all nodes in the connected component
            tmp = []
            visited[start] = True
            q = deque()
            q.append(start)
            while q:
                # Current node
                c = q.popleft()
                # Add to temporary component list
                tmp.append(c)
                # Check neighbors
                for val in self.adj[c]:
                    # If not visited
                    if not visited[val]:
                        visited[val] = True
                        q.append(val)
            # Return the found component
            return tmp

        # Iterate through all nodes to find all components
        for i in range(n):
            # If the node hasn't been visited
            if not visited[i]:
                # Perform BFS to fill the component
                x = bfs(i)
                # Add component to the list
                self.components.append(x)

    def bipartite_check(self, start: int, comp: List[int]) -> bool:
        # Check if the current component can be colored bipartitely
        # Initialize colors for the component
        color = {node: -1 for node in comp}
        q = deque([start])

        # Start coloring with 0
        color[start] = 0
        while q:
            # Current node
            node = q.popleft()
            for neigh in self.adj[node]:
                # Only process neighbors that belong to the current component
                if neigh not in color:
                    # Ignore nodes outside the component
                    continue
                # If uncolored
                if color[neigh] == -1:
                    # Color with opposite color
                    color[neigh] = 1 - color[node]
                    q.append(neigh)
                # If the same color, not bipartite
                elif color[neigh] == color[node]:
                    # Return False for non-bipartite
                    return False
        # Return True if bipartite
        return True

    def bfs(self, start: int, n: int) -> int:
        # BFS to count the number of nodes in the component
        tmp_comp_ans = 0
        # Reset visited for this BFS
        visited = [False] * n
        # Start from the current node
        q = deque([start])
        visited[start] = True
        
        while q:
            # Count the current node
            tmp_comp_ans += 1
            for _ in range(len(q)):
                # Current node to process
                curr = q.popleft()
                for neigh in self.adj[curr]:
                    # If neighbor is not visited
                    if not visited[neigh]:
                        # Add neighbor to queue
                        q.append(neigh)
                        # Mark as visited
                        visited[neigh] = True
        # Return the count for this BFS
        return tmp_comp_ans

sol = Solution()

n = 6
edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
#Expected Output 4
print(sol.magnificentSets(n, edges)) 
n = 3
edges = [[1,2],[2,3],[3,1]]
#Expected Output: -1

n = 92
edges = [[67,29],[13,29],[77,29],[36,29],[82,29],[54,29],[57,29],[53,29],[68,29],[26,29],[21,29],[46,29],[41,29],[45,29],[56,29],[88,29],[2,29],[7,29],[5,29],[16,29],[37,29],[50,29],[79,29],[91,29],[48,29],[87,29],[25,29],[80,29],[71,29],[9,29],[78,29],[33,29],[4,29],[44,29],[72,29],[65,29],[61,29]]      

#Expected Output: 57

n = 26
edges = [[9,16],[8,3],[20,21],[12,16],[14,3],[7,21],[22,3],[22,18],[11,16],[25,4],[2,4],[14,21],[23,3],[17,3],[2,16],[24,16],[13,4],[10,21],[7,4],[9,18],[14,18],[14,4],[14,16],[1,3],[25,18],[17,4],[1,16],[23,4],[2,21],[5,16],[24,18],[20,18],[19,16],[24,21],[9,3],[24,3],[19,18],[25,16],[19,21],[6,3],[26,18],[5,21],[20,16],[2,3],[10,18],[26,16],[8,4],[11,21],[23,16],[13,16],[25,3],[7,18],[19,3],[20,4],[26,3],[23,18],[15,18],[17,18],[10,16],[26,21],[23,21],[7,16],[8,18],[10,4],[24,4],[7,3],[11,18],[9,4],[26,4],[13,21],[22,16],[22,21],[20,3],[6,18],[9,21],[10,3],[22,4],[1,18],[25,21],[11,4],[1,21],[15,3],[1,4],[15,16],[2,18],[13,3],[8,21],[13,18],[11,3],[15,21],[8,16],[17,16],[15,4],[12,3],[6,4],[17,21],[5,18],[6,16],[6,21],[12,4],[19,4],[5,3],[12,21],[5,4]]

#Expected Output: 4

n = 30
edges = [[1,9],[30,27],[21,9],[2,10],[16,28],[1,27],[20,24],[22,24],[30,6],[30,19],[1,19],[30,11],[16,6],[16,29],[2,29],[2,23],[16,24],[1,25],[1,17],[16,23],[30,26],[16,12],[1,14],[13,23],[13,14],[2,19],[22,6],[30,3],[30,18],[20,8],[13,24],[20,9],[20,14],[13,28],[13,10],[2,8],[16,7],[16,10],[21,5],[20,15],[20,11],[2,26],[21,3],[22,10],[16,8],[2,17]]
 
#Expected Output: 8

n = 24
edges = [[2,13],[7,3],[5,3],[21,1],[5,1],[4,13],[21,19],[7,13],[15,3],[21,22],[17,19],[23,22],[14,13]]

#Expected Output: 19