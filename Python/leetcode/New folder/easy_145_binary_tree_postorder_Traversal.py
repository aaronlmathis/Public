# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.t = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            left = self.postorderTraversal(root.left)            
            right = self.postorderTraversal(root.right)

            self.t.append(root.val)

        return self.t
            