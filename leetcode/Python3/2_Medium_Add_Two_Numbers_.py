"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode(0)
        current = answer
        remainder = 0
        while l1 or l2 or remainder:
            curr_sum = remainder
            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next

            if curr_sum > 9:
                current.next = ListNode(curr_sum % 10)
                current = current.next
                remainder = 1

            else:
                current.next = ListNode(curr_sum)
                current = current.next
                remainder = 0
        
        return answer.next

        



l1 = [2,4,3]
l2 = [5,6,4]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]
def buildList(l: List[int]) -> ListNode:
    dummy = ListNode(0)
    current = dummy

    for num in l:
        current.next = ListNode(num)
        current = current.next
    
    head = dummy.next
    
    return head

l1, l2 = buildList(l1), buildList(l2)

sol = Solution()
print(sol.addTwoNumbers(l1, l2))