from math import gcd
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to print the linked list
def print_linked_list(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Example Usage


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current = head
        while current and current.next:
            g = gcd(current.val, current.next.val)
            new_node = ListNode(g)

            new_node.next = current.next
            current.next = new_node
            
            current = new_node.next
        return head

sol = Solution()
values = [18,6,10,3]
head = create_linked_list(values)
print("Original Linked List:")
print_linked_list(head)
res = sol.insertGreatestCommonDivisors(head)
print_linked_list(res)