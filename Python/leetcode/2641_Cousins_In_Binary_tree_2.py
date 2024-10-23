"""
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
from collections import deque, defaultdict
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        queue = deque()
        queue.append((root.val, root))
        
        while queue:
            n = len(queue)

            level_total = 0
            for local_total, node in queue:
                level_total += node.val

            for i in range(n):
                local_total, node = queue.popleft()   

                child_total = 0
                # Add left node to queue only if it exists.
                if node.left: child_total += node.left.val
                if node.right: child_total += node.right.val
            
                if node.left: queue.append((child_total, node.left))
                if node.right: queue.append((child_total, node.right))

                node.val = level_total - local_total
            
        return root

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(9)

root.left.left = TreeNode(1)
root.left.right = TreeNode(10)

root.right.right= TreeNode(7)

print(sol.replaceValueInTree(root))
