"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict
from typing import Optional, List

def create_binary_tree(nodes: List[int]) -> TreeNode:
    if not nodes:
        return None
    
    n = len(nodes)
    root = TreeNode(nodes[0])
    
    if n == 1:
        return root

    queue = deque([root])
    idx = 1

    while queue and idx < n - 1:
        node = queue.popleft()

        if idx < n and nodes[idx]:
            node.left = TreeNode(nodes[idx])
            queue.append(node.left)
        idx += 1

        if idx < n and nodes[idx]:
            node.right = TreeNode(nodes[idx])
            queue.append(node.right)
        idx+=1
    
    return root

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # Quick Exit: root is null
        if not root:
            return []
        
        # Keep track of maximum values seen in a level via hash map
        level_max = []

        # Create a queue (FIFO) to process nodes
        queue = deque((root))

        # While there are items in the queue
        while queue:
            n = len(queue)

            # curr_max holds the current maximum val for the level
            curr_max = float('-inf')

            # Iterate the length of the queue to ensure you process each node in the level before continuing while loop.
            for _ in range(n):
                # Pull the top level, node out of the queue
                node = queue.popleft()
                
                # Calculate the max val this level
                curr_max = max(curr_max, node.val)

                # If there is a left node, add it to queue 
                if node.left:
                    queue.append(node.left)

                # If there is a right node, add it to queue
                if node.right:
                    queue.append(node.right)
            
            # Add level maximum to answer
            level_max.append(curr_max)
        
        # Return list of level max val's
        return level_max

sol = Solution()
nodes = [1,3,2,5,3,None,9]
root = create_binary_tree(nodes)
print(sol.largestValues(root))