"""
There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.

You must connect one node from the first tree with another node from the second tree with an edge.

Return the minimum possible diameter of the resulting tree.

The diameter of a tree is the length of the longest path between any two nodes in the tree.

Example 1:
Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]
Output: 3
Explanation:
We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

Example 2:
Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
Output: 5
Explanation:
We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

"""
from typing import List
from collections import defaultdict, deque
from typing import List
from collections import defaultdict, deque

class Solution:   
    def get_diameter(self, n: int, edges: List[List[int]]) -> int:
        """
        Computes the diameter of a tree using the Leaf Trimming (Iterative Removal of Leaves) method.
        
        Args:
            n (int): Number of nodes in the tree.
            edges (List[List[int]]): List of edges where each edge is represented as [u, v].
        
        Returns:
            int: The diameter of the tree.
        """
        # Edge Case: Single-node tree has a diameter of 0
        if n == 1:
            return 0

        # Initialize adjacency list for the tree
        graph = [[] for _ in range(n)]
        # Initialize degree list to keep track of the number of connections for each node
        degree = [0] * n
        for v, w in edges:
            graph[v].append(w)
            graph[w].append(v)
            degree[v] += 1
            degree[w] += 1

        # Initialize deque with all leaf nodes (nodes with degree 1)
        leaves = deque(v for v in range(n) if degree[v] == 1)
        # Initialize tree size
        tree_size = n
        # Initialize radius to count the layers of leaves being trimmed
        radius = 0

        # Iteratively remove leaves until 2 or fewer nodes remain
        while tree_size > 2:
            # Number of leaves at the current layer
            leaves_count = len(leaves)
            for _ in range(leaves_count):
                # Remove a leaf from the deque
                leaf = leaves.popleft()
                # Decrement the tree size
                tree_size -= 1
                # Decrement the degree of the leaf
                degree[leaf] -= 1
                # Iterate through all neighbors of the leaf
                for neighbor in graph[leaf]:
                    # Decrement the degree of the neighbor since the leaf is removed
                    degree[neighbor] -= 1
                    # If the neighbor becomes a leaf, add it to the deque
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
            # Increment the radius after processing the current layer of leaves
            radius += 1

        # Calculate the diameter:
        # - If tree_size == 2, the diameter is 2 * radius + 1
        # - If tree_size == 1, the diameter is 2 * radius
        return 2 * radius + (tree_size == 2)
                
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:    
        """
        Connects two trees by adding an edge between any two nodes (one from each tree) to minimize the diameter of the resulting tree.
        
        Args:
            edges1 (List[List[int]]): Edge list of the first tree.
            edges2 (List[List[int]]): Edge list of the second tree.
        
        Returns:
            int: The minimum possible diameter of the merged tree.
        """    
        # Determine the number of nodes in each tree
        n, m = len(edges1) + 1, len(edges2) + 1    
        
        # Compute the diameters of both trees
        d1 = self.get_diameter(n, edges1)
        d2 = self.get_diameter(m, edges2)
        
        # Compute the radii of both trees
        # Radius is defined as ceil(diameter / 2)
        r1 = (d1 + 1) // 2
        r2 = (d2 + 1) // 2

        # The new diameter is the maximum of:
        # - The diameter of the first tree (d1)
        # - The diameter of the second tree (d2)
        # - The sum of the radii of both trees plus 1 (connecting edge)
        return max(d1, d2, 1 + r1 + r2)   
     


            
        





sol = Solution()
edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
print(sol.minimumDiameterAfterMerge(edges1, edges2))