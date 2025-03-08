""""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
"""

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(nodes: List[int])-> ListNode:
    if not nodes:
        return ListNode()
    
    head = ListNode()
    current = head
    for node in nodes:
        current.next = ListNode(node)
        current = current.next
    
    return head.next

def print_linked_list(head: ListNode) -> None:
    while head.next:
        print(f"{head.val}->",end="")
        head = head.next
    print(f"{head.val}")

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # List was empty.
        if not head:
            return 0
        # Build `vals` list by traversing linked list and recording node.val
        vals = []
        while head and head.next:
            vals.append(head.val)
            head = head.next
        vals.append(head.val)

        # Figure out `n` or the number of nodes
        n = len(vals)

        # Iterate from 0 to n // 2
        # Sum the node val with it's twin's val.
        # Record the max sum seen.
        max_sum = 0
        for i in range(n//2):
            s = vals[i]+vals[n-1-i]
            if s > max_sum:
                max_sum = s
        # Return it!
        return max_sum
        
        
sol = Solution()
nodes = [5,4,2,1]       
head = build_linked_list(nodes)
print(sol.pairSum(head))