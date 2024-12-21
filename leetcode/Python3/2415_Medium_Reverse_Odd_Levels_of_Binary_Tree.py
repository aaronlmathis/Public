"""
Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
Return the root of the reversed tree.

A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

The level of a node is the number of edges along the path between it and the root node.

Example 1:
Input: root = [2,3,5,8,13,21,34]
Output: [2,5,3,8,13,21,34]
Explanation: 
The tree has only one odd level.
The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.

Example 2:
Input: root = [7,13,11]
Output: [7,11,13]
Explanation: 
The nodes at level 1 are 13, 11, which are reversed and become 11, 13.

Example 3:
Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
Explanation: 
The odd levels have non-zero values.
The nodes at level 1 were 1, 2, and are 2, 1 after the reversal.
The nodes at level 3 were 1, 1, 1, 1, 2, 2, 2, 2, and are 2, 2, 2, 2, 1, 1, 1, 1 after the reversal.

"""
from typing import Optional, List
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def create_binary_tree(nodes: List[int]) -> TreeNode:
    if not nodes or nodes[0] is None:
        return None
    idx = 0
    n = len(nodes)
    root = TreeNode(nodes[idx])
    queue = deque([])
    queue.append(root)
    while queue:
        node = queue.popleft()
        if idx < n - 1 and nodes[idx+1] is not None:
            node.left = TreeNode(nodes[idx+1])
            queue.append(node.left)
        idx+=1
        if idx < n - 1 and nodes[idx+1] is not None:
            node.right = TreeNode(nodes[idx+1])
            queue.append(node.right)
        idx+=1
    return root

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def dfs(node1: TreeNode, node2: TreeNode, depth: int) -> None:
            # If either node is None, terminate recursion
            if not node1 or not node2:
                return
            
            # If we are at an odd level, swap the values
            if depth % 2 == 1:
                node1.val, node2.val = node2.val, node1.val
            
            # Recur for children: left of one with right of the other, and vice versa
            dfs(node1.left, node2.right, depth + 1)
            dfs(node1.right, node2.left, depth + 1)

        # Start DFS with the two children of the root
        dfs(root.left, root.right, 1)
        return root




        """ BFS / Queue Solution 
        # quick exit if root is null
        if not root:
            return None
        
        # Create a dictionary where key is level and value is list of node values.
        level_values = defaultdict(deque)

        queue = deque([])
        queue.append((0, root))
        while queue:
            level,  node = queue.popleft()
            if level % 2 != 0:
                level_values[level].append(node.val)
            if node.left:
                queue.append((level+1, node.left))
            if node.right:
                queue.append((level+1, node.right))

        queue.append((0, root))
        while queue:
            level,  node = queue.popleft()
            if level % 2 != 0:
                node.val = level_values[level].pop()
            if node.left:
                queue.append((level+1, node.left))
            if node.right:
                queue.append((level+1, node.right))
        return root
        """
        

sol = Solution()

nodes = list(range(1, 127))
root = create_binary_tree(nodes)
print(sol.reverseOddLevels(root))
