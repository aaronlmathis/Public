"""
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

Example 1:
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Example 2:
Input: preorder = [1], postorder = [1]
Output: [1]

Constraints:
1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
from collections import deque

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        queue = deque([])
        root = TreeNode(preorder[0])
        preorder = preorder[1:]
        postorder = postorder[:len(postorder)-1]

        if not preorder:
            return root
        
        x = 0
        while preorder[x] != postorder[-1]:
            x+=1
            
        pre_left_tree = preorder[0:x]
        post_left_tree = postorder[0:x]
        pre_right_tree = preorder[x:]
        post_right_tree = postorder[x:]

        if pre_left_tree:
            root.left = TreeNode(pre_left_tree[0])
            pre_left_tree = pre_left_tree[1:]
            post_left_tree = post_left_tree[:len(post_left_tree)-1]
            if pre_left_tree:
                queue.append((root.left, pre_left_tree, post_left_tree))

        if pre_right_tree:
            root.right = TreeNode(pre_right_tree[0])
            pre_right_tree = pre_right_tree[1:]
            post_right_tree = post_right_tree[:len(post_right_tree)-1]
            if pre_right_tree:
                queue.append((root.right, pre_right_tree, post_right_tree))



        while queue:
            curr, pre, post = queue.popleft()
            x = 0
            while pre[x] != post[-1]:
                x+=1
            
            pre_left_tree = pre[0:x]
            post_left_tree = post[0:x]
            pre_right_tree = pre[x:]
            post_right_tree = post[x:]
            
            if pre_left_tree:
                curr.left = TreeNode(pre_left_tree[0])
                pre_left_tree = pre_left_tree[1:]
                post_left_tree = post_left_tree[:len(post_left_tree)-1]
                if pre_left_tree:
                    queue.append((curr.left, pre_left_tree, post_left_tree))


            if pre_right_tree:
                curr.right = TreeNode(pre_right_tree[0])
                pre_right_tree = pre_right_tree[1:]
                post_right_tree = post_right_tree[:len(post_right_tree)-1]
                if pre_right_tree:
                    queue.append((curr.right, pre_right_tree, post_right_tree))

        return root


sol = Solution()
preorder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]
root = sol.constructFromPrePost(preorder, postorder)
