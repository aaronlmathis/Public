# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.lst = []

    def inorder_traversal(self, root: TreeNode):
        if root:
            self.inorder_traversal(root.left)
            self.lst.append(root.val)
            self.inorder_traversal(root.right)
            
    def sorted_list_to_BST(self, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(self.lst[mid])
        node.left = self.sorted_list_to_BST(start, mid-1)
        node.right = self.sorted_list_to_BST(mid+1, end)
        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.inorder_traversal(root)
        
        return self.sorted_list_to_BST(0, len(self.lst) - 1)

