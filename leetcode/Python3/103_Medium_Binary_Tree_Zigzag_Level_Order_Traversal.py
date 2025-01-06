"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 
"""
from typing import List, Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Quick exit if root is null
        if not root:
            return []
        
        queue = deque([root])
        ans = []

        dir = 0 # 0 = L -> R, 1 = R- > L
        while queue:
            # init level list to track level node vals.
            level = []
            
            # Iterate once for every node in queue (to process every node in the level.)
            for _ in range(len(queue)):
                # Pop the first node in
                node = queue.popleft()

                # If node.left exists, append it to queue
                if node.left:
                    queue.append(node.left)
                # If node.right exists, append it to the queue
                if node.right:
                    queue.append(node.right)
                
                # Add the current node's val
                level.append(node.val)
            
            # Append level orders to answer, Left to Right if dir = 0, Right to left if dir = 1
            if dir == 0:
                ans.append(level)
            else:
                ans.append(level[::-1])
            
            # Flip the direction
            dir = 0 if dir == 1 else 1
        
        # Return the answer
        return ans





root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.zigzagLevelOrder(root))        