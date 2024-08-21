# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        while head:
            next_node = head.next  # Save the next node
            head.next = new_head   # Reverse the link
            new_head = head        # Move new_head to the current node
            head = next_node       # Move to the next node in the list
        return new_head



