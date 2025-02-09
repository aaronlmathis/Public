"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 

Example 1:
Input: root1 = [3,5,1,6,2,9,8,None,None,7,4], root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
Output: true

Example 2:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
         


def create_tree(nodes: List[int]) -> TreeNode:
    if not nodes:  # Handle empty list case
        return None
    root = TreeNode(nodes[0])
    idx=1
    q = deque([root])
    n = len(nodes)
    while q and idx < n:    

            curr = q.popleft()
            
            if idx < n and nodes[idx] is not None:
                curr.left = TreeNode(nodes[idx])
                q.append(curr.left)
            idx+=1

            if idx < n and nodes[idx] is not None:
                curr.right = TreeNode(nodes[idx])
                q.append(curr.right)
            idx+=1
    
    return root


root1 = [3,5,1,6,2,9,8,None,None,7,4]
root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
root1 = create_tree(root1)
root2 = create_tree(root2)
sol = Solution()
print(sol.leafSimilar(root1, root2))