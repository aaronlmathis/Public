"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 
Constaints:
The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        even, odd = ListNode(), ListNode()

        curr_odd, curr_even = odd, even
        parity = False

        while head:
            if parity:
                curr_even.next = head
                curr_even = head
            else:
                curr_odd.next = head
                curr_odd = head

            parity = not parity
            head = head.next
        
        curr_odd.next = even.next
        curr_even.next = None

        return odd.next


nodes = [1,2,3,4,5]
nodes2 = [2,1,3,5,6,4,7]
head = build_linked_list(nodes)
head2 = build_linked_list(nodes2)
print_linked_list(head)
#print_linked_list(head2)
sol = Solution()
print(sol.oddEvenList(head))