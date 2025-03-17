"""
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""
from typing import List, Optional
from utils.single_linked_list import ListNode, SingleLinkedList

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def split(head: ListNode) -> ListNode:    
            slow = fast = head
            
            while fast and fast.next:
                fast = fast.next.next
                if fast:
                    slow = slow.next
            
            second = slow.next
            slow.next = None

            return second        
        
        def merge_sort(head: ListNode) -> ListNode:
            if not head or not head.next:
                return head
            second = split(head)
            head =  merge_sort(head)
            second = merge_sort(second)

            return merge(head, second)

        def merge(first: ListNode, second: ListNode) -> ListNode:
            if not first:
                return second
            if not second:
                return first
            
            if first.val < second.val:
                first.next = merge(first.next, second)
                return first
            else:
                second.next = merge(first, second.next)
                return second

        return merge_sort(head)       




sol = Solution()
nodes = [4,2,1,3]
head = SingleLinkedList.build_list(nodes)
SingleLinkedList.print_list(head)
print(sol.sortList(head))        