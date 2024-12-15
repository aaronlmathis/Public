"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
"""
from typing import Optional, List
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        queue = deque([])
        while head:
            print(head)
            queue.append(head)
            head = head.next
        for _ in range(k):
            tmp = queue.pop()
            queue.appendleft(tmp)

        newhead = ListNode(0)
        current = newhead
        while queue:
            current.next = queue.popleft()
            current = current.next

        current.next = None
        
        return newhead.next


nodes = [1,2,3,4,5] 
k = 2        

def createLinkedList(nodes: List[int]) -> ListNode:
    dummy = ListNode(0)
    current = dummy

    for node in nodes:
        current.next = ListNode(node)
        current = current.next
    
    return dummy.next

head = createLinkedList(nodes)
sol = Solution()
print(sol.rotateRight(head, k))