"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node_list = []
        while head:
            node_list.append(head)
            head = head.next

        left, right = left-1, right-1
        new_node_list = node_list[0:left]
        for i in range(right, left-1, -1):
            new_node_list.append(node_list[i])
        new_node_list+=node_list[right+1:]


        for i in range(len(new_node_list) - 1):
            new_node_list[i].next = new_node_list[i+1]

        new_node_list[len(new_node_list) - 1].next = None
        dummy = ListNode(0)
        current = dummy
        for node in new_node_list:
            current.next = node
            current = current.next

        return dummy.next

nodelist = [1,2,3,4,5]
def buildLinkedList(nodelist: list)-> ListNode:
    dummy = ListNode(0)
    current = dummy
    for node in nodelist:
        current.next = ListNode(node)
        current = current.next
    
    return dummy.next



head = buildLinkedList(nodelist)
left = 2
right = 4
sol = Solution()
print(sol.reverseBetween(head, left, right))