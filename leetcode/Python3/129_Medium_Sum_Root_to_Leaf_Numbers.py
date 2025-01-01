"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(node: TreeNode, current_path: Optional[List[int]] = None,all_paths: Optional[List[List[int]]] = None) -> List[List[int]]:
            if current_path is None:
                current_path = []
            if all_paths is None:
                all_paths = []

            if node is None:
                return all_paths

            current_path.append(node.val)

            if node.left is None and node.right is None:
                all_paths.append(list(current_path))
            else:
                if node.left:
                    traverse(node.left, current_path, all_paths)
                if node.right:
                    traverse(node.right, current_path, all_paths)

            current_path.pop()

            return all_paths
        
        ans = traverse(root)
        total = 0
        for a in ans:
            total+=int(''.join([str(num) for num in a]))
        return total
        
sol = Solution()
nodes = [1,2,3] 
root = build_tree(nodes)
print(sol.sumNumbers(root))       