"""
You are given an array pairs, where pairs[i] = [xi, yi], and:

There are no duplicates.
xi < yi
Let ways be the number of rooted trees that satisfy the following conditions:

The tree consists of nodes whose values appeared in pairs.
A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi is an ancestor of xi.
Note: the tree does not have to be a binary tree.
Two ways are considered to be different if there is at least one node that has different parents in both ways.

Return:

0 if ways == 0
1 if ways == 1
2 if ways > 1
A rooted tree is a tree that has a single root node, and all edges are oriented to be outgoing from the root.

An ancestor of a node is any node on the path from the root to that node (excluding the node itself). The root has no ancestors.

 

Example 1:


Input: pairs = [[1,2],[2,3]]
Output: 1
Explanation: There is exactly one valid rooted tree, which is shown in the above figure.
Example 2:


Input: pairs = [[1,2],[2,3],[1,3]]
Output: 2
Explanation: There are multiple valid rooted trees. Three of them are shown in the above figures.
Example 3:

Input: pairs = [[1,2],[2,3],[2,4],[1,5]]
Output: 0
Explanation: There are no valid rooted trees.
 

Constraints:

1 <= pairs.length <= 105
1 <= xi < yi <= 500
The elements in pairs are unique.
"""
from typing import List
from collections import defaultdict, deque
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:

        # Step 1: Construct the undirected graph
        graph = defaultdict(set)
        nodes = set()
        
        for a, b in pairs:
            graph[a].add(b)
            graph[b].add(a)
            nodes.update([a, b])  # Track all unique nodes
        
        # Step 2: Find valid root candidates
        root_candidates = []
        for node in nodes:
            if len(graph[node]) == len(nodes) - 1:  # Root must connect to all other nodes
                root_candidates.append(node)
        
        # Step 3: If no root exists, return 0; if multiple roots exist, return 2
        if not root_candidates:
            return 0
        if len(root_candidates) > 1:
            return 2  # Multiple roots → multiple trees
        
        root = root_candidates[0]  # Choose the only valid root
        
        # Step 4: Check for multiple valid trees using BFS
        parent_map = {}
        visited = set()
        queue = deque([(root, None)])  # (current_node, parent)
        
        while queue:
            node, parent = queue.popleft()
            
            if node in visited:
                return 0  # Cycle detected, invalid tree
            
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor == parent:  # Ignore back edge to parent
                    continue
                if neighbor in parent_map:  # Node already has a parent, ambiguity exists
                    return 2
                parent_map[neighbor] = node  # Assign parent
                queue.append((neighbor, node))
        
        # Step 5: If we visited all nodes, the tree is valid; otherwise, return 0
        return 1 if len(visited) == len(nodes) else 0


sol = Solution()
pairs = [[1,2],[2,3],[1,3]]
#pairs = [[1,2],[2,3],[2,4],[1,5]]
pairs = [[1,2],[2,3]]
#pairs = [[1,5],[1,3],[2,3],[2,4],[3,5],[3,4]]
print(sol.checkWays(pairs))