"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation:

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
Explanation:

Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
Input: root = []
Output: []
"""
from typing import Optional, List
from collections import deque, defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        level = 0
        level_vals = defaultdict(list)
        queue = deque([(0, root)])
        while queue:
            lvl, curr = queue.popleft()
            level_vals[lvl].append(curr.val)

            if curr.left:
                queue.append((lvl+1, curr.left))

            if curr.right:
                queue.append((lvl+1, curr.right))

        answer = []
        for lvl, nodes in level_vals.items():
            answer.append(nodes[-1])
        
        return answer
    
root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)

root.right = TreeNode(3)
root.right.right = TreeNode(4)
sol = Solution()
print(sol.rightSideView(root))