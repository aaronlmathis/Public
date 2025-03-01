"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""
from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If current node is None or p or q, return it. (either going to be a Treenode or None.)
        if not root or root == p or root == q:
            return root
        # Call function for left side of tree
        left = self.lowestCommonAncestor(root.left, p, q)
        # Call function for right side of tree.
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are not None, return this node
        if left and right:
            return root
        
        # Otherwise, return the non-null child
        return left if left else right

def build_tree(nodes):
    idx=1
    root = TreeNode(nodes[0])
    n = len(nodes)

    queue = deque([root])
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

nodes = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 1
root=  build_tree(nodes)

def dfs(node, p, q, pn=None, qn=None):
    if not node:
        return None, None
    if pn is not None and qn is not None:
        return (pn, qn)
    
    # Check if current node matches p or q
    pn = node if node.val == p else None
    qn = node if node.val == q else None

    # Recurse on left and right subtrees
    left_pn, left_qn = dfs(node.left, p, q)
    right_pn, right_qn = dfs(node.right, p, q)
    
    # Update pn and qn if found in left or right subtree
    pn = pn or left_pn or right_pn
    qn = qn or left_qn or right_qn

    return pn, qn

pn, qn = dfs(root, p, q, None, None)

sol = Solution()
print(sol.lowestCommonAncestor(root, pn, qn))
