class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import List

class SingleLinkedList:
    @staticmethod
    def build_list(nodes: List[int]) -> ListNode:
        head = ListNode()
        if len(nodes) < 1:
            return head
        head.val = nodes[0]
        curr = head
        for i in range(1, len(nodes)):
            curr.next = ListNode(nodes[i])
            curr = curr.next
        return head
    @staticmethod
    def print_list(head: ListNode) -> None:
        if not head:
            print('Empty List')
            return
        while head.next:
            print(f"{head.val}->", end='')
            head = head.next
        print(f"{head.val}")

        
            