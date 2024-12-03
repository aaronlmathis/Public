"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 
"""
from typing import Optional, List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



def createBinaryTree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    index = 1  # Start from the second value
    
    while index < len(values):
        current = queue.pop(0)  # Get the next node to add children
        
        # Add the left child if there's a value
        if index < len(values):
            current.left = TreeNode(values[index])
            queue.append(current.left)
            index += 1
        
        # Add the right child if there's a value
        if index < len(values):
            current.right = TreeNode(values[index])
            queue.append(current.right)
            index += 1
    
    return root

p = [1,2,3]
q = [1,2,3]
p = createBinaryTree(p)
q = createBinaryTree(q)

sol = Solution()
print(sol.isSameTree(p, q))