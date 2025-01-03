"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import deque
def build_tree(nodes: List[int]) -> TreeNode:
    if not nodes:
        return None
    
    n = len(nodes)
    root = TreeNode(nodes[0])
    idx = 1
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if idx < n and nodes[idx] is not None:
            node.left = TreeNode(nodes[idx])
            queue.append(node.left)
        idx+=1

        if idx < n and nodes[idx] is not None:
            node.right = TreeNode(nodes[idx])
            queue.append(node.right)
        idx+=1

    return root


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')
        
        def in_order_traversal(node: Optional[TreeNode]):
            """Performs in-order traversal and updates min_diff."""
            if not node:
                return
            
            # Traverse left subtree
            in_order_traversal(node.left)
            
            # Process current node
            if self.prev is not None:
                current_diff = node.val - self.prev
                if current_diff < self.min_diff:
                    self.min_diff = current_diff
            self.prev = node.val  # Update previous node's value
            
            # Traverse right subtree
            in_order_traversal(node.right)
        
        in_order_traversal(root)
        return self.min_diff

nodes =[236,104,701,None,227,None,911]
root = build_tree(nodes)
sol = Solution()
print(sol.getMinimumDifference(root))        