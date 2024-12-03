"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(1, root)])
        maxLevel = 0

        while queue:
            level, current = queue.popleft()
            maxLevel = max(level, maxLevel)

            if current:
                if current.left:
                    queue.append((level + 1, current.left))
                
                if current.right:
                    queue.append((level + 1, current.right))


        return maxLevel if maxLevel > 0 else 0



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

nums = [1,None,2]
root = createBinaryTree(nums)
sol = Solution()
print(sol.maxDepth(root))