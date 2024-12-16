"""
You are given an array nums consisting of positive integers.
Starting with score = 0, apply the following algorithm:
    - Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
    - Add the value of the chosen integer to score.
    - Mark the chosen element and its two adjacent elements if they exist.
    - Repeat until all the array elements are marked.

    Return the score you get after applying the above algorithm.

Example 1:
Input: nums = [2,1,3,4,5,2]
Output: 7
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,1,3,4,5,2].
- 2 is the smallest unmarked element, so we mark it and its left adjacent element: [2,1,3,4,5,2].
- 4 is the only remaining unmarked element, so we mark it: [2,1,3,4,5,2].
Our score is 1 + 2 + 4 = 7.

Example 2:
Input: nums = [2,3,5,1,3,2]
Output: 5
Explanation: We mark the elements as follows:
- 1 is the smallest unmarked element, so we mark it and its two adjacent elements: [2,3,5,1,3,2].
- 2 is the smallest unmarked element, since there are two of them, we choose the left-most one, so we mark the one at index 0 and its right adjacent element: [2,3,5,1,3,2].
- 2 is the only remaining unmarked element, so we mark it: [2,3,5,1,3,2].
Our score is 1 + 2 + 2 = 5.
"""
from typing import List
import heapq
from collections import deque

class Solution:
    def findScore(self, nums: List[int]) -> int:
        """
        Priority Queue (Min Heap Solution)

        score = 0
        n = len(nums)
        min_heap = []
        marked = set()
        for index, value in enumerate(nums):
            heapq.heappush(min_heap, (value, index))

        while min_heap:
            value, index = heapq.heappop(min_heap)
            if index not in marked:
                score+=value
                if index > 0:
                    marked.add(index-1)
                if index < n-1:
                    marked.add(index+1)
        return score
        
        score = 0
        nums_idx = [(value, index) for index, value in enumerate(nums)]
        nums_idx.sort(key=lambda x: (x[0], x[1]))
        marked = set()

        for value, index in nums_idx:
            if index not in marked:
                score+=value
                if index > 0:
                    marked.add(index-1)
                if index < len(nums_idx)-1:
                    marked.add(index+1)
                
        return score
        """

        score = 0  # Initialize the total score
        n = len(nums)
        q = deque()  # Initialize a deque to process elements

        for i in range(n):
            # If the deque is not empty and the current number is >= last in deque
            if q and nums[i] >= q[-1]:
                skip = False  # Initialize skip flag for alternating additions
                # Process the deque
                while q:
                    add = q.pop()  # Remove elements from the deque (from the end)
                    if not skip:
                        score += add  # Add to the score if skip is False
                    skip = not skip  # Alternate between adding and skipping
                continue  # Move to the next number in the list

            # Otherwise, add the current number to the deque
            q.append(nums[i])

        # Process any remaining elements in the deque after the loop
        skip = False
        while q:
            add = q.pop()
            if not skip:
                score += add
            skip = not skip  # Alternate between adding and skipping

        return score  # Return the final computed score

nums = [2,1,3,4,5,2]
sol = Solution()
print(sol.findScore(nums))