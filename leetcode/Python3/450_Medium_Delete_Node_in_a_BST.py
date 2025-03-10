"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:
Input: root = [], key = 0
Output: []
 

Constraints:
"""
from utils.binary_tree import TreeNode, BinaryTree
from typing import List, Optional
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Empty Tree - return None
        if not root:
            return None

        def searchBST(root, parent=None, d=-1):
            """         
            Helper DFS function for searching Binary Search Tree. 
            Args:
                - root: Optional[TreeNode] - the root of the tree to search
                - parent: Optional[TreeNode] - the parent node of the current node
                - d: int = -1 - the direction taken from parent->current node. 1=Left, 0=Right
            Returns:
                - tuple (node: Optional[TreeNode], parent: Optional[TreeNode], d: int)
            """
            if not root:
                return (None, None, None)
            if root.val == key:
                return (root, parent, d)
            elif root.val > key:
                return searchBST(root.left, root, 1)
            else:
                return searchBST(root.right, root, 0)

        node, parent, d = searchBST(root)

        # Key not found
        if not node:
            return root

        print(f'Deleting {node.val}, Parent: {parent.val if parent else "None"}, Direction: {d}')

        # Case 1: The node has **no children** (leaf node)
        if not node.left and not node.right:
            if parent:
                if d:
                    parent.left = None
                else:
                    parent.right = None
            else:
                return None  # If root itself is deleted
            del node

        # Case 2: The node has **two children**
        elif node.left and node.right:
            # Find inorder successor (smallest in right subtree)
            successor_parent = node
            successor = node.right
            while successor.left:
                successor_parent = successor
                successor = successor.left

            # Copy successor's value to current node
            node.val = successor.val

            # Remove successor
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
            
            del successor
        # Case 3: The node has **one child**
        else:
            child = node.left if node.left else node.right
            if parent:
                if d:
                    parent.left = child
                else:
                    parent.right = child
            else:
                root = child  # If root is being deleted, new root becomes the child
            del node
        return root
    
sol = Solution()
nodes = [5,3,6,2,4,None, 7]
key = 3
root = BinaryTree.build_tree(nodes)
new = sol.deleteNode(root, key)

print(BinaryTree.print_tree(new))