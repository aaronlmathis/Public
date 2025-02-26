"""
We run a preorder depth-first search (DFS) on the root of a binary tree.
At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.
If a node has only one child, that child is guaranteed to be the left child.
Given the output traversal of this traversal, recover the tree and return its root.

Example 1:
Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:
Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:
Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]

Constraints:
The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 109
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import defaultdict, deque

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []  # Stack to track parent nodes at each depth
        i = 0
        n = len(traversal)

        while i < n:
            depth = 0  # Count dashes
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            value = 0  # Parse integer value
            while i < n and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(value)  # Create node
            
            if depth == len(stack):
                # This is a left child
                if stack:
                    stack[-1].left = node
            else:
                # This is a right child, pop until we find its parent
                while len(stack) > depth:
                    stack.pop()
                stack[-1].right = node
            
            stack.append(node)  # Push this node to stack

        return stack[0]  # The root is the first element in the stack

traversal = "1-2--3--4-5--6--7"
sol = Solution()
print(sol.recoverFromPreorder(traversal))        