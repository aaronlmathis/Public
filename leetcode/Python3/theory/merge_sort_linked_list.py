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