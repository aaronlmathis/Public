# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total_tilt = 0
    
    def traverse_and_compute(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_sum = self.traverse_and_compute(root.left)
        right_sum = self.traverse_and_compute(root.right)
        
        # Compute the tilt for the current node
        tilt = abs(left_sum - right_sum)
        
        # Add the tilt of the current node to the total tilt
        self.total_tilt += tilt
        
        # Return the sum of values of the current subtree
        return left_sum + right_sum + root.val

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.traverse_and_compute(root)
        return self.total_tilt
  
        