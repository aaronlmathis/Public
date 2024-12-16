"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10
 
"""
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0]
        
        n = len(triangle)
        costs = [[0 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        costs[n-1] = triangle[n-1]

        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                costs[i][j] = triangle[i][j] + min(costs[i+1][j], costs[i+1][j+1])

        return costs[0][0]

sol = Solution()
triangle = [[2],
            [3,4],
            [6,5,7],
            [4,1,8,3]]
print(sol.minimumTotal(triangle))        
"""
costs = [
    [11],
    [9, 10],
    [7, 6, 10],
    [4, 1, 8, 3]
]
"""