"""
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
Return an array of the k parts.
"""
from typing import List, Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def generate_linked_list(values):
    if not values:  # If the list is empty, return None
        return None

    # Create the head of the linked list
    head = ListNode(values[0])
    current = head

    # Loop through the rest of the values and create nodes
    for value in values[1:]:
        current.next = ListNode(value)  # Create a new node and link it
        current = current.next  # Move to the next node

    return head  # Return the head of the linked list


# Example usage
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
linked_list = generate_linked_list(values)


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        total_length = 0
        current = head
        while current:
            total_length += 1
            current = current.next

        # Step 2: Determine the size of each part
        quotient, remainder = divmod(total_length, k)

        parts = []
        current = head

        for i in range(k):
            part_size = quotient + (1 if i < remainder else 0)  # Add 1 extra node to the first 'remainder' parts
            part_head = current  # This is the head of the current part

            # Traverse 'part_size - 1' nodes (because current is already the head)
            for j in range(part_size - 1):
                if current:
                    current = current.next

            # If there are nodes in the current part, break the link to the next part
            if current:
                next_part = current.next  # Temporarily store the next node
                current.next = None  # Break the link to split the part
                current = next_part  # Move to the next part

            parts.append(part_head)  # Append the current part to the result list

        return parts

sol = Solution()
k = 3
print(sol.splitListToParts(linked_list, k))