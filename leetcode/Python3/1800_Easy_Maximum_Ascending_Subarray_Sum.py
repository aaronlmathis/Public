"""
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

Example 2:
Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
 
"""
from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Let n be the length of nums
        n = len(nums)

        # Keep a running and max sum as you iterate
        # Set both initially to nums[0].
        rsum = msum = nums[0]

        # Iterate over nums, starting at 1.
        for i in range(1, n):
            # If nums[i] is greater than nums[i-1], add it to running sum
            if nums[i] > nums[i-1]:
                rsum+=nums[i]
            # It's not, so start the ascending total over.
            else:
                rsum = nums[i]
            # Every iteration, set msum to the max of msum and rsum (to keep track of largest sum seen)
            msum = max(msum, rsum)
        # Return msum
        return msum




sol = Solution()
nums = [100,10,1]
print(sol.maxAscendingSum(nums))        