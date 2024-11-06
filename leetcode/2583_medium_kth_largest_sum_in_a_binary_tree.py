"""
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = {}
        if not root:
            return -1  # Return -1 or some indication for an invalid tree
        
        queue = deque([(root, 0)])  # Use deque for efficient popping
        while queue:
            node, level = queue.popleft()  
            
            # Update the sum for the current level
            level_sums[level] = level_sums.get(level, 0) + node.val
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        # Sort sums in descending order
        sorted_sums = sorted(level_sums.values(), reverse=True)
        
        # Check if k is valid
        if k <= len(sorted_sums):
            return sorted_sums[k-1]  # Return the k-th largest sum
        else:
            return -1  # Return -1 if k is out of range

# Function to insert nodes in level order
def insertLevelOrder(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        
        # insert left child
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        
        # insert right child
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    
    return root

def printTree(root):
    if not root:
        return
    queue = [(root, 0)]
    current_level = 0
    while queue:
        node, level = queue.pop(0)
        if level > current_level:
            print()  # Move to next level
            current_level = level
        print(f"{node.val} ", end="")
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    print()  # For final newline


# Test case example
# Tree: [5, 8, 9, 2, 1, 3, 7]
arr = [5, 8, 9, 2, 1, 3, 7]
k=2
n = len(arr)
root = None
root = insertLevelOrder(arr, root, 0, n)
sol = Solution()

print(sol.kthLargestLevelSum(root, k))