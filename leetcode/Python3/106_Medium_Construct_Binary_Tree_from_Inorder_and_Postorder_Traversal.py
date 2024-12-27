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
        root_val = postorder[-1]
        root_idx = inorder.index(root_val)

        left_tree = inorder[:root_idx]
        right_tree = inorder[root_idx+1:]

        print(f"{left_tree} - {right_tree}")

        root = TreeNode(root_val)

        if len(left_tree) > 0:
            root.left = TreeNode(left_tree[0])
            queue = deque([root.left])
            l_idx = 1
            while queue:
                curr_node = queue.popleft()

                if len(left_tree) > l_idx and left_tree[l_idx]:
                    curr_node.left = TreeNode(left_tree[l_idx])
                    queue.append(curr_node.left)
                l_idx+=1
                
                if len(left_tree) > l_idx and left_tree[l_idx]:
                    curr_node.right = TreeNode(left_tree[l_idx])
                    queue.append(curr_node.right)
                l_idx+=1

        if len(right_tree) > 0:
            root.right = TreeNode(right_tree[0])
            queue = deque([root.right])
            r_idx = 1
            while queue:
                curr_node = queue.popleft()

                if len(right_tree) > r_idx and right_tree[r_idx]:
                    curr_node.right = TreeNode(right_tree[r_idx])
                    queue.append(curr_node.right)
                r_idx+=1
                
                if len(right_tree) > r_idx and right_tree[r_idx]:
                    curr_node.right = TreeNode(right_tree[r_idx])
                    queue.append(curr_node.right)
                r_idx+=1                
        return root

sol = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(sol.buildTree(inorder, postorder))

nodes = [3,9,20,None,None,15,7]        