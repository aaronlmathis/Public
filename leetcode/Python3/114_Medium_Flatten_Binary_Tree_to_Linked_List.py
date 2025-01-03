"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 
"""
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes: List[int]) -> TreeNode:
    if not nodes:
        return None
    
    n = len(nodes)
    root = TreeNode(nodes[0])
    idx = 1
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if idx < n and nodes[idx] is not None:
            node.left = TreeNode(nodes[idx])
            queue.append(node.left)
        idx+=1

        if idx < n and nodes[idx] is not None:
            node.right = TreeNode(nodes[idx])
            queue.append(node.right)
        idx+=1

    return root

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        def traverse(node):
            if not node or node is None:
                return
            
            print(node.val)
            nodes.append(node)

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)
        
        traverse(root)
        
        for i in range(len(nodes)):

            root.left = None
            root.right = nodes[i+1] if i < len(nodes)-1 else None
            root = root.right



sol = Solution()
nodes = [1,2,5,3,4,None,6]    
root = build_tree(nodes)    
print(sol.flatten(root))