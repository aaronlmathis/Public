"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        nstart, nend = newInterval[0], newInterval[1]

        # Binary search to find the correct position for newInterval
        def binarySearch(nstart) -> int:
            left, right = 0, len(intervals)
            while left < right:
                mid = left + (right - left) // 2
                if intervals[mid][0] < nstart:
                    left = mid + 1
                else:
                    right = mid
            return left

        idx = binarySearch(nstart)
        intervals.insert(idx, newInterval)

        # Merge overlapping intervals
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result

intervals =[[1,5]]
#[1,2], [3,5], [4,8], [6,7], [8,10], [12,16]
# 0 1    0 1    0 1    0 1    0 1      0 1
#  0      1      2      3      4        5
#
newInterval = [2,3]
sol = Solution()
print(sol.insert(intervals, newInterval))        