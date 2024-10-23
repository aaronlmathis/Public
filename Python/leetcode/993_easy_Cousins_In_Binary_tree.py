"""
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        current_level = 0
        cousinx, cousiny = None, None
        def traverse(level: int, node: TreeNode, parent:TreeNode = None):
            nonlocal cousinx, cousiny
            if not node:
                return
            if node.val == x:
                cousinx = (level, parent)
            if node.val == y:
                cousiny = (level, parent)
            if node.left:
                traverse(level+1, node.left, node)
            if node.right:
                traverse(level+1, node.right, node)                
        if not root:
            return -1
        
        traverse(current_level,root)

        levelx, parentx = cousinx
        levely, parenty = cousiny

        if (levelx == levely) and (parentx is not parenty):
            return True

        return False

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
#root = [1,2,3,4]
x = 4
y = 3        
print(sol.isCousins(root, x, y))
