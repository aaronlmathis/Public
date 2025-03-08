"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 
Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000
"""
from typing import List, Optional
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case: One way to have sum = targetSum

        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val  # Update the current path sum
            count = prefix_sums[curr_sum - targetSum]  # Check if there's a valid prefix sum
            
            # Store the current sum in the hashmap
            prefix_sums[curr_sum] += 1
            
            # Recur into left and right children
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            # Backtrack: Remove the current path sum count
            prefix_sums[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)

    
sol = Solution()
nodes = [1,-2,-3,1,3,-2,None,-1]
idx = 1
root = TreeNode(nodes[0])
queue = deque([root])
while queue:
    curr = queue.popleft()
    if idx < len(nodes) and nodes[idx] is not None:
        curr.left = TreeNode(nodes[idx])
        queue.append(curr.left)
    idx+=1

    if idx < len(nodes) and nodes[idx] is not None:
        curr.right = TreeNode(nodes[idx])
        queue.append(curr.right)
    idx+=1

targetSum = -1
print(sol.pathSum(root, targetSum))