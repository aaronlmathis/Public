# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

      
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        fast = head
        for i in range(n):
            fast = fast.next
        
        while fast.next:
            print(current.val)
            current = current.next
            fast = fast.next
            
        current.next = current.next.next
        return current

# Example Usage
values = [1,2,3,4,5]
head = create_linked_list(values)
print_linked_list(head)  
n = 2
sol = Solution()
print(sol.removeNthFromEnd(head, n))