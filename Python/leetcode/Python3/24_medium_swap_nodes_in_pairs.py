# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to help with edge cases
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        if not head:
            return None

        if not head.next:
            return head
        
        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            
            # Perform the swap
            first.next = second.next
            second.next = first
            current.next = second
            
            # Move current pointer forward by 2 nodes
            current = first
        
        return dummy.next
