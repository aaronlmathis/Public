"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
 

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

"""
from collections import deque, defaultdict

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = deque([root])
        level = 0
        while queue:
            print(f"Level: {level}")
            lvl_queue = deque([])
            for _ in range(len(queue)):
                curr = queue.popleft()
                print(f"N: {curr.val} - {curr.next.val if curr.next != None else 'None'}\t", end="")
                if curr.left:
                    queue.append(curr.left)
                    lvl_queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    lvl_queue.append(curr.right)
            while lvl_queue:
                left_node = lvl_queue.popleft()
                if lvl_queue:
                    right_node = lvl_queue.popleft()
                    left_node.next = right_node
                    lvl_queue.appendleft(right_node)
                else:
                    left_node.next = None
                    

            level+=1
            print()
nodes = [1,2,3,4,5,None,7]
root = Node(nodes[0])
idx = 1
queue = deque([root])
while queue:
    curr = queue.popleft()

    if idx < len(nodes) and nodes[idx] is not None:
        curr.left = Node(nodes[idx])
        queue.append(curr.left)
    idx+=1
    if idx < len(nodes) and nodes[idx] is not None:
        curr.right = Node(nodes[idx])
        queue.append(curr.right)
    idx+=1

sol = Solution()
print(sol.connect(root))