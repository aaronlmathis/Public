"""
You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
"""
from typing import List, Optional
from collections import deque
import copy
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depths = {}
        heights = {}
        
        # Step 1: Compute heights and depths using DFS
        def compute_heights(node, depth):
            if not node:
                return -1
            depths[node.val] = depth
            left_height = compute_heights(node.left, depth + 1)
            right_height = compute_heights(node.right, depth + 1)
            heights[node.val] = 1 + max(left_height, right_height)
            return heights[node.val]
        
        compute_heights(root, 0)
        
        # Step 2: Precompute the maximum heights for each level excluding subtrees
        max_height_without_subtree = {}
        level_max_height = {}
        
        # Collect the max heights for each depth level
        def update_level_heights(node):
            if not node:
                return
            depth = depths[node.val]
            if depth not in level_max_height:
                level_max_height[depth] = []
            level_max_height[depth].append(heights[node.val])
            update_level_heights(node.left)
            update_level_heights(node.right)
        
        update_level_heights(root)
        
        # Sort each level's heights in descending order to allow easy access to the top two heights
        for depth in level_max_height:
            level_max_height[depth].sort(reverse=True)
        
        # Compute maximum height of the tree excluding each node's subtree
        for node_val in heights:
            depth = depths[node_val]
            max_heights = level_max_height[depth]
            
            # Determine the max height excluding the subtree at this node
            if len(max_heights) == 1:
                max_height_without_subtree[node_val] = depth - 1
            elif heights[node_val] == max_heights[0]:
                max_height_without_subtree[node_val] = depth + (max_heights[1] if len(max_heights) > 1 else 0)
            else:
                max_height_without_subtree[node_val] = depth + max_heights[0]
        
        # Step 3: Answer each query
        return [max_height_without_subtree[q] for q in queries]
sol = Solution()

root = TreeNode(1)
root.right = TreeNode(5)
root.right.left = TreeNode(3)
root.right.left.left = TreeNode(2)
root.right.left.right = TreeNode(4)

queries = [3,5,4,2,4]

print(sol.treeQueries(root, queries))

"""

        def dfs(node: TreeNode, h: int) -> int:
            if not node:
                return h
            left_height = dfs(node.left, h+1)
            right_height = dfs(node.right, h+1)
            
            return max(left_height, right_height)
        
        def remove_subtree(node: TreeNode, val: int):
            if not node:
                return None

            # Check if the left or right child is the target node
            if node.left and node.left.val == val:
                node.left = None
                return
            if node.right and node.right.val == val:
                node.right = None
                return
            
            # Recursively search for the target node
            remove_subtree(node.left, val)
            remove_subtree(node.right, val)            

        
        result = []
        for query in queries:
            # Create a deep copy of the root for each query
            node_copy = copy.deepcopy(root)
            remove_subtree(node_copy, query)
            result.append(dfs(node_copy, 0) - 1)

        return result


"""