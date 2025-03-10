class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List
from collections import deque
class BinaryTree:
    @staticmethod
    def build_tree(nodes: List[int]) -> TreeNode:
        if len(nodes) == 0:
            return TreeNode()
        root = TreeNode(nodes[0])
        idx = 1
        n = len(nodes)
        queue = deque([root])
        while queue:
            node = queue.popleft()

            if idx < n and nodes[idx] is not None:
                node.left = TreeNode(nodes[idx])
                queue.append(node.left)
            idx+=1

            if idx <n and nodes[idx] is not None:
                node.right = TreeNode(nodes[idx])
                queue.append(node.right)
            idx+=1
        return root
   
    @staticmethod
    def print_tree(root: TreeNode, level=0, prefix="Root: "):
        """ Recursively prints a binary tree in ASCII format """
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.val))
            if root.left or root.right:
                if root.left:
                    BinaryTree.print_tree(root.left, level + 1, "L--> ")
                else:
                    print(" " * ((level + 1) * 4) + "L--> None")
                    
                if root.right:
                    BinaryTree.print_tree(root.right, level + 1, "R--> ")
                else:
                    print(" " * ((level + 1) * 4) + "R--> None")