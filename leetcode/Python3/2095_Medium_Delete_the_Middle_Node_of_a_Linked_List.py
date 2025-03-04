"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
 

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

def build_linked_list(nodes)-> ListNode:
    head = ListNode(1)
    curr = head
    for i in range(1, len(nodes)):
        curr.next = ListNode(nodes[i])
        #print(nodes[i])
        curr = curr.next
    return head

def print_linked_list(head: ListNode)-> List[int]:
    linked_list = []
    while head:
        linked_list.append(head.val)
        head = head.next 
    return linked_list   
from collections import defaultdict
import math
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        middle = math.floor(count / 2)

        curr = head
        #print(middle)
        for _ in range(middle-1):
            curr = curr.next
        curr.next = curr.next.next

        return head





nodes = [1,3,4,7,1,2,6]
head = build_linked_list(nodes)
sol = Solution()
print(sol.deleteMiddle(head))