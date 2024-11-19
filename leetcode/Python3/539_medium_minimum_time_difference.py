"""
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
"""
from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_minutes(time: str) -> int:
            # Convert "HH:MM" to total minutes from 00:00
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes        
        
        # Convert all times to minutes
        minutes = sorted(time_to_minutes(time) for time in timePoints)
        # Initialize min_diff to a large number
        min_diff = float('inf')
    
        # Compare adjacent times in the sorted list
        for i in range(1, len(minutes)):
            # Difference between consecutive times
            diff = minutes[i] - minutes[i - 1]
            min_diff = min(min_diff, diff)

        # Check wrap-around difference between last and first time
        # 1440 minutes in a day, so calculate the backward difference
        wrap_around_diff = (1440 + minutes[0] - minutes[-1]) % 1440
        min_diff = min(min_diff, wrap_around_diff)
        
        return min_diff

sol = Solution()
timePoints = ["00:00","23:59","00:00"]
print(sol.findMinDifference(timePoints))