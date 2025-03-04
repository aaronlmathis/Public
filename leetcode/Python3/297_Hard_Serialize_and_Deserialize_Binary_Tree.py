"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(nodes: List[int]) -> TreeNode:
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
    return root

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            
            if node is not None:
                serial.append(str(node.val))
                serial.append('&')
            else:
                serial.append('*')
                serial.append('&')
                continue
            
            queue.append(node.left)

            queue.append(node.right)
       
        return ''.join(serial)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        nodes = data.split('&')
        print(nodes)
        n = len(nodes)
        idx = 1
        root = TreeNode(nodes[0])
        queue = deque([root])
        while queue:
            node = queue.popleft()

            if idx < n and nodes[idx] != '*':
                node.left = TreeNode(nodes[idx])
                queue.append(node.left)
            idx+=1

            if idx < n and nodes[idx] != '*':
                node.right = TreeNode(nodes[idx])
                queue.append(node.right)
            idx+=1

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
nodes =[4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
root = build_tree(nodes)
ser = Codec()
deser = Codec()
print(deser.deserialize(ser.serialize(root)))