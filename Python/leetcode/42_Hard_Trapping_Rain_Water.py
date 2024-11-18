"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # Helper function that produces two arrays, maxLeft and maxRight, giving the max left/right value for every number in height
        def findMaximums(nums):
            n = len(nums)
            if n == 0:
                return [], []

            # Precompute the maximum values to the left and right
            maxLeft = [0] * n
            maxRight = [0] * n

            # Populate max_left
            maxLeft[0] = float('-inf')  # No value to the left of the first element
            for i in range(1, n):
                maxLeft[i] = max(maxLeft[i - 1], nums[i - 1])

            # Populate max_right
            maxRight[-1] = float('-inf')  # No value to the right of the last element
            for i in range(n - 2, -1, -1):
                maxRight[i] = max(maxRight[i + 1], nums[i + 1])

            return maxLeft, maxRight
        
        maxLeft, maxRight = findMaximums(height)    # Create two lists with maximum values to the left and right of each value in height.
        result = 0                                  # The answer to to problem
        n = len(height)                             # Initialize n as length of heights

        for i in range(n):                          # Iterate through each height, calculating how much water that position holds.
            # Take the minimum maximum of the heights at the left and right boundaries.
            minMaxBoundary = min(maxLeft[i], maxRight[i])
            
            # Calculate how much water this position will hold.
            # water = min(L, R) - h[i]
            water = minMaxBoundary - height[i]

            # If water is positive (can't have negative water) add it to result.
            if water > 0:
                result+=water
        
        return result

sol = Solution()
height = [4,2,0,3,2,5]
print(sol.trap(height))