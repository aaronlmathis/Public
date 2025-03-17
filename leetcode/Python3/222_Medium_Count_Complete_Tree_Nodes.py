"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""
from utils.binary_tree import TreeNode, BinaryTree
from collections import deque
from typing import List, Optional
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1 
        if not root.left or not root.right:
            return 2
        
        node_count = 0
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                node_count+=1
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return node_count


nodes = [1,None,1]
root = BinaryTree.build_tree(nodes)
sol = Solution()
print(sol.countNodes(root))