"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
 

Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 
Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from utils.binary_tree import TreeNode, BinaryTree

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        """max_path = float('-inf')
        roots = {root}
        def find_path(parent, node, total, visited):
            nonlocal max_path

            max_path = max(max_path, total)

            # Choice 1 - left
            if node.left:
                if node.left not in visited:
                    visited.add(node.left)
                    find_path(node, node.left, total+node.left.val, visited)
                    visited.remove(node.left)
                if node.left not in roots:
                    roots.add(node.left)    
                    find_path(node, node.left, node.left.val, {node.left})
                

            # Choice 2 - right
            if node.right:
                if node.right not in visited:
                    visited.add(node.right)
                    find_path(node, node.right, total+node.right.val, visited)
                    visited.remove(node.right)
                if node.right not in roots:
                    roots.add(node.right)
                    find_path(node, node.right, node.right.val, {node.right})    
            
            
            # Choice 3 - Up
            if parent is not None:
                if parent not in visited:
                    visited.add(parent)
                    find_path(node, parent, total+parent.val, visited)
                    visited.remove(parent)
                if parent not in roots:
                    roots.add(parent)
                    find_path(None, parent, parent.val, {parent})
            
        find_path(None, root, root.val, {root})
        return max_path        
"""     
        max_path = float('-inf')
        roots = {root}
        def find_path(start, parent, node, total, visited, path):
            nonlocal max_path

            max_path = max(max_path, total)
            print(f"start: {start.val} crr: {node.val} {path} Total: {total}")

            right, left = 0,0
            # Choice 1 - left
            if node.left and node.left not in visited:
                visited.add(node.left)
                path.append(node.left.val)
                find_path(start, node, node.left, total+node.left.val, visited, path)
                visited.remove(node.left)
                path.pop()
            if node.left and node.left not in roots:
                roots.add(node.left)    
                find_path(node.left, node, node.left, node.left.val, {node.left}, [node.left.val])
                

            # Choice 2 - right
            if node.right and node.right not in visited:
                visited.add(node.right)
                path.append(node.right.val)
                find_path(start, node, node.right, total+node.right.val, visited, path)
                path.pop()
                visited.remove(node.right)
            if node.right and node.right not in roots:
                roots.add(node.right)
                find_path(node.right, node, node.right, node.right.val, {node.right}, [node.right.val])    
            
            
            # Choice 3 - Up
            if parent is not None:
                if parent not in visited:
                    visited.add(parent)
                    path.append(parent.val)
                    find_path(start, node, parent, total+parent.val, visited, path)
                    visited.remove(parent)
                    path.pop()
                if parent not in roots:
                    roots.add(parent)
                    find_path(parent, None, parent, parent.val, {parent}, [parent.val])
            
        find_path(root, None, root, root.val, {root}, [root.val])
        return max_path


nodes = [-10,9,20,None,None,15,7]   
nodes = [5,4,8,11,None,13,4,7,2,None,None,None,1]
root = BinaryTree.build_tree(nodes)
sol = Solution()
print(sol.maxPathSum(root))