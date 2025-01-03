"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]
 
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        # Create a hashmap to store value -> index relations for inorder traversal
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}
        
        # Initialize a pointer to the last element in postorder traversal
        self.post_idx = len(postorder) - 1

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            if in_left > in_right:
                return None

            # Pick the current root value from postorder traversal
            root_val = postorder[self.post_idx]
            self.post_idx -= 1

            # Create the root node
            root = TreeNode(root_val)

            # Root splits inorder list into left and right subtrees
            index = inorder_index_map[root_val]

            # Important: build the right subtree before the left subtree
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)

            return root
        
        return helper(0, len(inorder) - 1)

sol = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(sol.buildTree(inorder, postorder))

nodes = [3,9,20,None,None,15,7]        