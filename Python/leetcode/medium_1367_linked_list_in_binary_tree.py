# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(tree_node: TreeNode, list_node: ListNode) -> bool:
            if not list_node:  # If we have matched all the linked list nodes
                return True
            if not tree_node:  # If we reached the end of the tree branch
                return False
            if tree_node.val != list_node.val:  # Values don't match
                return False
            # Recursively check the left and right subtrees
            return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)

        # Traverse the tree and try to start a path from each node
        if not root:
            return False
        # Start a DFS from the root or any other node in the tree
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)        