"""
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

"""
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False
        
        return (
            # Non-flipped: left matches left and right matches right
            self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            or
            # Flipped: left matches right and right matches left
            self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        )


sol = Solution()
root1 = TreeNode(1)

root1.left = TreeNode(2)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(8)

root1.right = TreeNode(3)
root1.right.left = TreeNode(6)

root2 = TreeNode(1)
root2.left = TreeNode(3)
root2.left.right = TreeNode(6)

root2.right = TreeNode(2)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(5)
root2.right.right.left = TreeNode(8)
root2.right.right.right = TreeNode(7)

print(sol.flipEquiv(root1, root2))