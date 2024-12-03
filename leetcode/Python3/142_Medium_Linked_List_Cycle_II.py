"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import List, Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break
        else:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

def createCyclicLinkedList(linkedList: list, pos: int) -> ListNode:
    dummy = ListNode(0)  # Dummy node
    current = dummy
    cycle_start = None  # Pointer to the node where the cycle starts
    
    for i, value in enumerate(linkedList):
        new_node = ListNode(value)
        current.next = new_node
        current = current.next
        if i == pos:
            cycle_start = new_node  # Mark the start of the cycle
    
    if pos != -1:
        current.next = cycle_start  # Create the cycle
    
    return dummy.next  # Return the head of the actual list

head = []
linkedLists = [[3,2,0,-4], [1,2], [1]]
pos = [1,0,-1]

for i in range(len(linkedLists)):
    head.append(createCyclicLinkedList(linkedLists[i], pos[i]))


sol = Solution()
for i in range(len(head)):
    print(f"Test Case: {i+1}")
    print(sol.detectCycle(head[i]))