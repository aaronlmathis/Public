"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize: 
        #   n as length of nums
        #   start as left boundary of window (zero)
        #   subTotal sum of subarray as zero
        #   minLength as n + 1 (at end, if minLength > n, we know that zero should be returned because list items don't total target)
        n = len(nums)
        start = 0
        subTotal = 0
        minLength = n+1

        # Iterate through nums dynamically, using sliding window
        for end in range(0, n):
            # Calculate sum total of subarray by adding nums[end] to subTotal
            subTotal += nums[end]
            # While subTotal >= target number, calculate length of subarray
            # set minLength to length if length < minLength
            # Shrink window by increasing start after reducing subTotal by nums[start]
            while subTotal >= target:
                length = end - start + 1
                if length < minLength:
                    minLength = length
                subTotal -= nums[start]
                start+=1

        # Return 0 if minLength > n (meaning we never found a subarray whose sum > target)
        # Otherwise return minLength       
        return 0 if minLength > n else minLength


sol = Solution()
target = 4
nums = [1,4,4]
print(sol.minSubArrayLen(target, nums))