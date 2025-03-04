"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 

Example 1:


Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:


Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 5 * 104].
1 <= Node.val <= 100
"""
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        
        max_len = 0

        # Use Iterative DFS - (current node, last direction, length) 0 = left, 1 = right
        dfs = []
        if root.left:
            dfs.append((root.left, 0, 1))
        if root.right:
            dfs.append((root.right, 1, 1))
        
        while dfs:
            curr, dir, len = dfs.pop()

            if not curr:
                continue

            max_len = max(max_len, len)
            # If the last direction was left, go right
            if dir == 0:
                dfs.append((curr.right, 1, len+1))
                dfs.append((curr.left,0, 1 ))

            else:
                dfs.append((curr.left, 0, len+1))
                dfs.append((curr.right,1, 1 ))
      
        return max_len
def build_tree(nodes):
    idx = 1
    root = TreeNode(nodes[0])
    queue = deque([root])
    n = len(nodes)
    while queue:
        curr = queue.popleft()
        if idx < n and nodes[idx] is not None:
            curr.left = TreeNode(nodes[idx])
            queue.append(curr.left)
        idx+=1
        if idx < n and nodes[idx] is not None:
            curr.right = TreeNode(nodes[idx])
            queue.append(curr.right)
        idx+=1
    return root
 

nodes = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1]    
root = build_tree(nodes)   
sol = Solution()
print(sol.longestZigZag(root))
from graphviz import Digraph

def draw_tree(root, name="Binary Tree"):
    dot = Digraph(name)
    def add_nodes_edges(node):
        if node:
            dot.node(str(node.val))
            if node.left:
                dot.edge(str(node.val), str(node.left.val))
                add_nodes_edges(node.left)
            if node.right:
                dot.edge(str(node.val), str(node.right.val))
                add_nodes_edges(node.right)
    add_nodes_edges(root)
    return dot
dot = draw_tree(root)
dot.render("tree", format="png", view=True)  # Saves and opens image