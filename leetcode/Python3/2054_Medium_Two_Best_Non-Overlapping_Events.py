"""
You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

Example 1:
Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.

Example 2:
Example 1 Diagram
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.

Example 3:
Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
"""
from typing import List
import heapq
from bisect import bisect_right
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        max_values = [0]
        max_values_ends = [-1]

        events.sort(key = lambda x: x[1])

        max_val= 0
        for start, end, value in events:
            index = bisect_right(max_values_ends, start - 1) - 1
            
            if value + max_values[index] > max_val:
                max_val = value + max_values[index]
            if value > max_values[-1]:
                max_values.append(value)
                max_values_ends.append(end)
        
        return max_val

            

#events = [[1,3,2],[4,5,2],[2,4,3]]  # 4
events = [[1,3,2],[4,5,2],[1,5,5]] # 5
#events = [[1,5,3],[1,5,1],[6,6,5]] # 8
sol = Solution()
print(sol.maxTwoEvents(events))