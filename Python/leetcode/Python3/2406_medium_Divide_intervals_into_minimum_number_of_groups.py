"""
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].
You have to divide the intervals into one or more groups such that each interval is in exactly one group, 
and no two intervals that are in the same group intersect each other.
Return the minimum number of groups you need to make.
Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.

Example 1:
Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
Explanation: We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.

Example 2:
Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
Output: 1
Explanation: None of the intervals overlap, so we can put all of them in one group.
"""
import heapq
from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals by the first point of each interval
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        # Step 2: Initialize an empty min-heap (priority queue)
        min_heap = []
        #Step 3: Push the end time of the first interval into the heap.
        heapq.heappush(min_heap, sorted_intervals[0][1])
        #Step 4: Iterate through intervals, comparing the start time of the interval with the top iteam of the heap. If the start time is greater or equal
        # to the top item of the heap, pop the top item of the heap. Then push the end time into the heap.
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] > min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, sorted_intervals[i][1])
        #Step 5: Return the size of the heap as the number of groups.
        return len(min_heap)

sol = Solution()
print(sol.minGroups(intervals))
