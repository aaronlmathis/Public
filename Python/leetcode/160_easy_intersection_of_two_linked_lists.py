# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        :type head1, head1: ListNode
        :rtype: ListNode
        
        stackA = []
        stackB = []

        if headA is headB:
            return headA
        
        if not headA.next and not headB.next and headA is headB:
            return headA

        if not headA.next and headB.next:
            while headB.next:
                stackB.append(headB)
                headB= headB.next
            b = stackB.pop()
            if headA is b:
                print("Dammit")
                return b

        if not headB.next and headA.next:

            while headA.next:
                stackA.append(headA)
                headA= headA.next
            if headB is stackA.pop():
                return headB


        while headA.next: #iterate through both lists till the end.
            stackA.append(headA)
            headA = headA.next
        while headB.next:
            stackB.append(headB)
            headB= headB.next
        
        if not stackA or not stackB:
            return None

        if stackA[-1] is not stackB[-1]:
            return None

        while stackA and stackB:
            a = stackA.pop()
            b = stackB.pop()
            if a is not b:
                a = a.next
                b = b.next
                return a
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        hash_set = set()
        while headA:
            hash_set.add(headA)
            headA = headA.next
        while headB:
            if headB in hash_set:
                return headB
            headB = headB.next
