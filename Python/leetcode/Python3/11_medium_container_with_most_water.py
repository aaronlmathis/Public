"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Use a 2-pointer approach to track left and right boundary
        left, right = 0, len(height)-1

        # Track the maximum volume seen
        maxArea = 0

        # Iterate while left boundary is still left or at right boundary.
        while left <= right:

            # The width of the water container is the right boundary minus the left
            width = right - left

            # Calculate the min height between left and right, to see maximum height of container
            maxHeight = min(height[left], height[right])

            # Calculate the volume as width * maxHeight
            area = width * maxHeight

            # Track the max volume seen
            maxArea = max(area, maxArea)

            # Move the pointer that is smaller, if left then move right, if right then move left.
            if height[left] > height[right]:
                right-=1
            else:
                left+=1

        # Return the largest volume
        return maxArea
        


height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(height))        