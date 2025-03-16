"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 

Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""
from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        def kadane(arr):
            max_ending_here = max_so_far = arr[0]
            for num in arr[1:]:
                max_ending_here = max(num, max_ending_here + num)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far

        total_sum = sum(nums)
        max_kadane = kadane(nums)
        min_kadane = kadane([-num for num in nums])  # Find min subarray sum

        max_circular = total_sum + min_kadane  # max circular sum is total_sum - min subarray sum

        if max_circular == 0:  # Handles edge case where all numbers are negative
            return max_kadane

        return max(max_kadane, max_circular)

sol = Solution()
nums = [1, -2, 3, -2]
nums = [5,-3, 5]
nums = [21,2,6,-53,5,4,3]
print(sol.maxSubarraySumCircular(nums))