# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> [ListNode]:
        vector = []
        while list1:
            vector.append(list1.val)
            list1 = list1.next

        while list2:
            vector.append(list2.val)
            list2 = list2.next

        # Sorting the list
        vector.sort()

        # Creating a new list with sorted values
        temp = ListNode(-1)
        head = temp
        for value in vector:
            temp.next = ListNode(value)
            temp = temp.next
        head = head.next

        # Returning the resultant linked list
        return head
        