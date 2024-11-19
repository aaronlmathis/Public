"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
"""
from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Calculate the initial slope
        if coordinates[1][0] - coordinates[0][0] == 0:  # Vertical line
            slope = float('inf')
        else:
            slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        
        # Iterate through the coordinates, checking if each segment has the same slope
        for i in range(1, len(coordinates) - 1):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i + 1]
            
            # Calculate the new slope
            if x2 - x1 == 0:  # Vertical line
                new_slope = float('inf')
            else:
                new_slope = (y2 - y1) / (x2 - x1)
            
            # If slopes don't match, return False
            if new_slope != slope:
                return False
        
        return True
sol = Solution()
coordinates = [[2,1],[4,2],[6,3]]
print(sol.checkStraightLine(coordinates))