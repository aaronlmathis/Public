"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 
"""
from typing import List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_testcase(nodes):
    n = len(nodes)
    root = TreeNode(nodes[0])
    queue = deque([root])
    idx = 1
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

    return root
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"{fname} took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper
class Solution:
    @timed
    def goodNodes(self, root: TreeNode) -> int:
        """        
        queue = deque([(root, root.val)])
        good_nodes = 0
        while queue:
            node, curr_max = queue.popleft()

            if node.val >= curr_max:
                good_nodes+=1
                curr_max = node.val
            
            if node.left is not None:
                queue.append((node.left, curr_max))
            if node.right is not None:
                queue.append((node.right, curr_max))
        return good_nodes    
        
        """
        self.__good_nodes = 0
        def traverse(node: int, path_max: int) -> None:
            if not node:
                return
            if node.val >= path_max:
                path_max = node.val
                self.__good_nodes+=1

            traverse(node.left, path_max)
            traverse(node.right, path_max)
        traverse(root, root.val)
        return self.__good_nodes

sol = Solution()
nodes = [3,3,None,4,2]
#nodes = [3,1,4,3,None,1,5]
nodes = [2,None,4,10,8,None,None,4]
nodes =[-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3]
"""
        2
       / \
    None  4
         / \
        10  8
           /
          4
"""
root = create_testcase(nodes)        
print(sol.goodNodes(root))