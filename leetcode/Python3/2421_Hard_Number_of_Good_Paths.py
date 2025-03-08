"""
There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

1. The starting node and the ending node have the same value.
2. All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).

Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.
 

Example 1:
Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation: There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].

Example 2:
Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
Output: 7
Explanation: There are 5 good paths consisting of a single node.
There are 2 additional good paths: 0 -> 1 and 2 -> 3.

Example 3:
Input: vals = [1], edges = []
Output: 1
Explanation: The tree consists of only one node, so there is one good path.
 

Constraints:

n == vals.length
1 <= n <= 3 * 104
0 <= vals[i] <= 105
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.
"""
from typing import List
from collections import defaultdict
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # Function to find the root (with path compression for efficiency)
        def find_root(node):
            if parent[node] != node:
                parent[node] = find_root(parent[node])  # Path compression
            return parent[node]

        # Function to merge two sets and count "good paths"
        def union(node1, node2):
            root1, root2 = find_root(node1), find_root(node2)

            if root1 != root2:  # Only merge if they are in different sets
                # Ensure root1 is the larger set (union by size)
                if size[root1] < size[root2]:
                    root1, root2 = root2, root1

                # Merge root2 into root1
                parent[root2] = root1
                size[root1] += size[root2]

                # If both roots had the same value, count good paths
                if max_value[root1] == max_value[root2]:
                    path_count = count[root1] * count[root2]
                    count[root1] += count[root2]
                    return path_count
                
                # If root2 has a higher value, update root1's max value & count
                elif max_value[root1] < max_value[root2]:
                    max_value[root1], count[root1] = max_value[root2], count[root2]
                    
            return 0  # No new paths formed

        # Initialization
        n = len(vals)
        total_paths = n  # Each node is a trivial "good path" by itself
        parent = list(range(n))  # Union-Find parent array
        size = [1] * n  # Size of each component
        max_value = vals[:]  # Track max value in each component
        count = [1] * n  # Number of nodes with max value in each component

        # Sort edges by the **maximum** node value in each pair
        edges.sort(key=lambda e: max(vals[e[0]], vals[e[1]]))

        # Process edges in order, merging components and counting good paths
        for node1, node2 in edges:
            total_paths += union(node1, node2)

        return total_paths
sol = Solution()
vals = [1,3,2,1,3]
edges = [[0,1],[0,2],[2,3],[2,4]]        
#vals =[2,2,5,5]
#edges =[[1,0],[0,2],[3,2]]
print(sol.numberOfGoodPaths(vals, edges))