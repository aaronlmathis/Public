"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict
from typing import Optional, List
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        level = 0
        level_vals = defaultdict(list)
        queue = deque([(0, root)])

        while queue:
            lvl, current = queue.popleft()
            level_vals[lvl].append(current.val)

            if current.left:
                queue.append((lvl+1, current.left))
            if current.right:
                queue.append((lvl+1, current.right))

        answer = []

        for lvl, nodes in level_vals.items():
            avg = 0
            for node in nodes:
                avg+=node
            answer.append(avg / len(nodes))
        return answer
root = TreeNode(3)
root.left = TreeNode(9)

root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.averageOfLevels(root))