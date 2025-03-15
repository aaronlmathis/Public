"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
 

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 
Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from utils.binary_tree import TreeNode, BinaryTree

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_path = float('-inf')

        def find_path(node):
            nonlocal max_path

            if not node:
                return 0
            
            # Return max path of left tree, exclude negatives
            left = max(find_path(node.left), 0)
            right = max(find_path(node.right), 0)

            max_path = max(max_path, node.val + left + right)

            return node.val + max(left, right)
        
        find_path(root)
        return max_path

nodes = [-10,9,20,None,None,15,7]   
nodes = [5,4,8,11,None,13,4,7,2,None,None,None,1]
nodes = [-10,9,20,None,None,15,7]   
root = BinaryTree.build_tree(nodes)
sol = Solution()
print(sol.maxPathSum(root))