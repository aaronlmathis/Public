# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty, just return None
        if not head:
            return None
        
        # Start with the head node
        current = head
        
        # Traverse the list
        while current and current.next:
            # If the current value is the same as the next value, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Otherwise, move to the next node
                current = current.next
        
        # Return the modified list
        return head