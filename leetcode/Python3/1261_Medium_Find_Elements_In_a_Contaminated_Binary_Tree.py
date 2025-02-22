"""
Given a binary tree with the following rules:

root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.
 

Example 1:


Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 
Example 2:


Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
Example 3:


Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
 

Constraints:

TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 104]
Total calls of find() is between [1, 104]
0 <= target <= 106
"""
from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_binary_tree(nodes) -> TreeNode:
    if not nodes:
        return TreeNode()
    
    idx=1
    n = len(nodes)

    root = TreeNode(-1)
    queue = deque([root])

    while queue:
        curr = queue.popleft()

        if idx < n and nodes[idx] is not None:
            curr.left = TreeNode(nodes[idx])
            queue.append(curr.left)
        idx+=1
        
        if idx < n and nodes[idx] is not None:
            curr.right = TreeNode(nodes[idx])
            queue.append(curr.right)
        idx+=1
    
    return root


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        """
        Initializes the FindElements object.

        Args:
            root (TreeNode): The contaminated binary tree to find elements in.
        
        """
        self.__tree_values = set()
        
        def dfs(node, val):
            if not node:
                return
            
            self.__tree_values.add(val)
            dfs(node.left, 2 * val + 1)
            dfs(node.right, 2 * val + 2)
        
        dfs(root, 0)
        

    def find(self, target: int) -> bool:
        """
        Returns true if the target value exists in the recovered binary tree.

        Args:
            target (int): The target value to find in the recovered binary tree.
        """
        return target in self.__tree_values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
nodes = [-1,None, -1]
root = build_binary_tree(nodes)
obj = FindElements(root)
print(obj.find(1))
print(obj.find(2))
print(obj.find(3))