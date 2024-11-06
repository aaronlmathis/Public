"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 
"""# Definition for a binary tree node.
from typing import List, Optional
from collections import deque, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        max_sum = float('-inf')  # Track the maximum sum
        max_level = 0            # Track the level with the maximum sum
        current_level = 1        # Track the current level
        queue = deque([root])    # Initialize the queue with the root node
        
        # BFS traversal
        while queue:
            level_sum = 0  # Sum of the current level
            for _ in range(len(queue)):  # Process all nodes at the current level
                node = queue.popleft()
                level_sum += node.val
                
                # Add the children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Check if the current level sum is the maximum
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            
            current_level += 1  # Move to the next level
        
        return max_level


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)

root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)
print(sol.maxLevelSum(root))