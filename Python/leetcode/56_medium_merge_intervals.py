"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])

        merged_intervals = []
        current_interval = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= current_interval[1]:
                current_interval[1] = max(current_interval[1], intervals[i][1])
            else:
                merged_intervals.append(current_interval)
                current_interval = intervals[i]

        merged_intervals.append(current_interval)

        return merged_intervals

        """
            print(f"{intervals[i]} {intervals[j]}")
            if intervals[i][1] >= intervals[j][0]:
                res.append([intervals[i][0],intervals[j][1]])
                j+=2
                i+=2
            elif intervals[i][0] <= intervals[j][0]:
                res.append([intervals[j][0],intervals[j][1]])
                j+=2
                i+=2  
            else:
                res.append(intervals[i])
                res.append(intervals[j])
                j+=1
                i+=1
        """
  

sol = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(intervals)) # [[1,6],[8,10],[15,18]]
intervals = [[1,4],[0,4]]
print(sol.merge(intervals)) # [[1,5]]