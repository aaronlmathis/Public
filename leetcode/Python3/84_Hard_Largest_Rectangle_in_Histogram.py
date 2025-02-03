"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
 
Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
"""
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        left_bound, left_stack = [-1] * n, []
        right_bound, right_stack = [n] * n, []
        
        for i in range(n):
            while left_stack and heights[left_stack[-1]] >= heights[i]:
                left_stack.pop()
            if not left_stack:
                left_bound[i] = -1
            else:
                left_bound[i] = left_stack[-1]
            left_stack.append(i)
        
        for i in range(n-1, -1, -1):
            while right_stack and heights[right_stack[-1]] >= heights[i]:
                right_stack.pop()
            if not right_stack:
                right_bound[i] = n
            else:
                right_bound[i] = right_stack[-1]
            right_stack.append(i)
     


        max_area = 0
        for i in range(n):
            width = right_bound[i] - left_bound[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area
sol = Solution()
heights = [2,1,5,6,2,3]        
print(sol.largestRectangleArea(heights))