"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

"""
from typing import List, Optional
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None
        def traverse(node):
            if not node or self.res is not None:
                return
            
            traverse(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            traverse(node.right)
        traverse(root)

        return self.res
    

nodes = [3,1,4,None,2]
nodes = [5,3,6,2,4,None,None,1]
root = build_tree(nodes)
k = 3       
sol = Solution()
print(sol.kthSmallest(root, k))