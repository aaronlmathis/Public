"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
from typing import List
from collections import defaultdict
from math import gcd
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(x1,y1,x2,y2):
            if x1 == x2:
                return float('inf')
            return (y2-y1) / (x2 - x1)
      
        max_points = 0

        if len(points) <= 2:
            return len(points)

        for i in range(len(points)):
            slope_dict = {}
            for j in range(i+1,len(points)):
                if i != j:
                    currSlope = slope(points[i][0] , points[i][1] , points[j][0] , points[j][1])
                    slope_dict[currSlope] = slope_dict.get(currSlope , 1) + 1
            
            if len(slope_dict) >= 1:
                max_points = max(max_points, max(slope_dict.values()))
        
        return max_points

sol = Solution()
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]       
print(sol.maxPoints(points)) 