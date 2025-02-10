"""
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 
Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 """
from typing import List
from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        
        tree = [set() for _ in range(n)]
        for a,b in edges:
            tree[a].add(b)
            tree[b].add(a)
        
        leaves = [i for i in range(n) if len(tree[i])==1]
        remaining = n
        
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = tree[leaf].pop()
                tree[neighbor].remove(leaf)
                if len(tree[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
    """
        if n <= 2:
            return list(range(n))

        tree = defaultdict(list)
        for a,b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        num_edges = [len(tree[i]) for i in range(n)]
        queue = deque([i for i in range(n) if num_edges[i] == 1])
        nodes = set(i for i in range(n))
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                nodes.remove(curr)

                for neighbor in tree[curr]:
                    num_edges[neighbor]-=1
                    if num_edges[neighbor] == 1:
                        queue.append(neighbor)
            if len(nodes) <= 2:
                return list(nodes)    
    
    """
sol = Solution()
n = 4
edges = [[1,0],[1,2],[1,3]]  
print(sol.findMinHeightTrees(n, edges))