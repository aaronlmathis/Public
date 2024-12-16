"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 
"""
from typing import Optional, List
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p1 = deque()
        p2 = deque()

        while head:
            if head.val < x:
                p1.append(head)
            else:
                p2.append(head)
            
            head = head.next
        
        dummy = ListNode(0)
        current = dummy

        while p1:
            current.next = p1.popleft()
            current = current.next
        
        while p2:
            current.next = p2.popleft()
            current = current.next

        current.next = None

        return dummy.next
    


def createLinkedList(nodes: List[int]) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    for node in nodes:
        current.next = ListNode(node)
        current = current.next

    return dummy.next



sol = Solution()
nodes = [1,4,3,2,5,2]
head = createLinkedList(nodes)
x = 3        
print(sol.partition(head, x))